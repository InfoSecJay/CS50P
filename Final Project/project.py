"""
    Author: Jay Tymchuk (@JayInfoSec)
    Scrape Elastic, SigmaHQ and Splunk GitHub threat detection rule repositories and export them to individual CSVs.
"""

import os
import csv
import requests
import yaml
import toml
from datetime import datetime
from dotenv import load_dotenv
from requests.exceptions import RequestException
import logging
import argparse

# Load environment variables
load_dotenv()

# GitHub repository URL and token
SPLUNK_GITHUB_API_URL = "https://api.github.com/repos/splunk/security_content/contents/detections"
SIGMAHQ_GITHUB_API_URL = "https://api.github.com/repos/SigmaHQ/sigma/contents/rules"
ELASTIC_GITHUB_API_URL = "https://api.github.com/repos/elastic/detection-rules/contents/rules"
ELASTIC_BBR_GITHUB_API_URL = "https://api.github.com/repos/elastic/detection-rules/contents/rules_building_block"
GITHUB_TOKEN = os.getenv("github_token")

# List of files to exclude due to abnormal contents resulting in parsing issues
EXCLUDED_FILES = {
    "driver_load_win_mal_drivers.yml",
    "driver_load_win_mal_drivers_names.yml",
    "driver_load_win_vuln_drivers.yml",
    "driver_load_win_vuln_drivers_names.yml",
    "defense_evasion_masquerading_windows_dll.toml"
}

# Get the current date
CURRENT_DATE = datetime.now().strftime("%d_%m_%Y")

# Configure logging to both console and output log file
LOG_FILE = f"rules_export_log_{CURRENT_DATE}.log"
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE, mode='w', encoding='utf-8'),
        logging.StreamHandler()
    ]
)

# Initialize a session for persistent connections
session = requests.Session()
session.headers.update({"Authorization": f"token {GITHUB_TOKEN}"})

def main(repositories: list[str]) -> None:
    """Main function to fetch, parse, and export YAML/TOML data into CSV for multiple repositories."""
    
    if not GITHUB_TOKEN:
        logging.error("GitHub token not found. Please check your .env file.")
        return

    # Define supported repositories with their respective API URLs and file extensions.
    repo_config = {
        "splunk": (SPLUNK_GITHUB_API_URL, ".yml"),
        "sigmahq": (SIGMAHQ_GITHUB_API_URL, ".yml"),
        "elastic": (ELASTIC_GITHUB_API_URL, ".toml"),
        "elastic_bbr": (ELASTIC_BBR_GITHUB_API_URL, ".toml")
    }

    total_files = 0
    total_failed = 0

    for repo in repositories:
        api_url, file_extension = repo_config.get(repo, (None, None))

        if not api_url:
            logging.warning(f"Invalid repository: {repo}. Skipping...")
            continue

        logging.info(f"Exporting: {repo} detection rule repository")
        
        # Get data and counts
        data, repo_files, repo_failed = scrape_files(api_url, repo, file_extension)
        total_files += repo_files
        total_failed += repo_failed

        if data:
            write_to_csv(data, repo)
        else:
            logging.warning(f"No {file_extension.upper()} files were fetched for {repo}.")

    # Log summary of total files and failures
    logging.info(f"Summary: Total files scanned: {total_files}, Total failed files: {total_failed}")

def fetch_content(url, repository):
    """Fetch YAML/TOML content from a given URL given a repository name."""
    try:
        response = session.get(url)
        response.raise_for_status()
        if repository == "sigmahq" or repository == "splunk":
            return yaml.safe_load(response.text)   # Return the raw YAML content
        else:
            return response.text  # Return the raw TOML content
    except RequestException as e:
        logging.error(f"Error fetching {url}: {e}")
        return None

def scrape_files(url, repository, file_extension):
    """Recursively fetch and parse YAML or TOML files from the specified repository."""
    try:
        response = session.get(url)
        response.raise_for_status()
        data = response.json()
    except RequestException as e:
        logging.error(f"Failed to fetch data from {url}: {e}")
        return [], 0, 0  # No files, so return zero counts

    parsed_data = []
    file_count = 0
    failed_count = 0

    for item in data:
        if item["type"] == "file" and item["name"].endswith(file_extension):
            file_count += 1
            file_url = item["download_url"]
            file_content = fetch_content(file_url, repository)

            if file_content:
                logging.info(f"Fetching and parsing {item['name']}...")
                if file_extension == ".yml":
                    parsed = parse_yaml_content(file_content, item, repository)
                elif file_extension == ".toml":
                    parsed = parse_toml_content(file_content, item)
                if parsed:
                    parsed_data.append(parsed)
                else:
                    failed_count += 1
            else:
                failed_count += 1

        elif item["type"] == "dir":
            logging.info(f"Entering directory: {item['name']}")
            nested_data, nested_count, nested_failed = scrape_files(item["url"], repository, file_extension)
            parsed_data.extend(nested_data)
            file_count += nested_count
            failed_count += nested_failed

    return [data for data in parsed_data if data], file_count, failed_count  # Return counts as well as parsed data

def parse_yaml_content(content, item, repository):
    """Parse YAML content and return relevant fields based on the repository."""
    rule_folder_location = os.path.dirname(item["path"])
    rule_file_name = item["name"]

    if rule_file_name in EXCLUDED_FILES:
        logging.info(f"Skipping {rule_file_name} (excluded).")
        return None

    if repository == "splunk":
        tags = content.get("tags", {})
        return {
            "GitHub Folder Location": rule_folder_location,
            "GitHub File Name": rule_file_name,
            "Name": content.get("name", ""),
            "ID": content.get("id", ""),
            "Version": content.get("version", ""),
            "Date": content.get("date", ""),
            "Author": content.get("author", ""),
            "Status": content.get("status", ""),
            "Type": content.get("type", ""),
            "Description": content.get("description", ""),
            "Data Source": content.get("data_source", ""),
            "Search": content.get("search", ""),
            "How To Implement": content.get("how_to_implement", ""),
            "Known False Positives": content.get("known_false_positives", ""),
            "References": content.get("references", ""),
            "Analytic Story": tags.get("analytic_story", ""),
            "Confidence": tags.get("confidence", ""),
            "Impact": tags.get("impact", ""),
            "Risk Score": tags.get("risk_score", ""),
            "Message": tags.get("message", ""),
            "MITRE ATT&CK ID": tags.get("mitre_attack_id", ""),
        }
    elif repository == "sigmahq":
        logsource = content.get("logsource", {})
        return {
            "GitHub Folder Location": rule_folder_location,
            "GitHub File Name": rule_file_name,
            "Title": content.get("title", ""),
            "ID": content.get("id", ""),
            "Status": content.get("status", ""),
            "Description": content.get("description", ""),
            "Date": content.get("date", ""),
            "Modified": content.get("modified", ""),
            "Tags": content.get("tags", ""),
            "Product": logsource.get("product", ""),
            "Category": logsource.get("category", ""),
            "Service": logsource.get("service", ""),
            "Author": content.get("author", ""),
            "Detection": content.get("detection", ""),
            "Falsepositives": content.get("falsepositives", ""),
            "Level": content.get("level", ""),
        }

def parse_toml_content(content, item):
    """Parse TOML content and return relevant fields, skipping excluded files."""
    
    rule_file_name = item["name"]

    if rule_file_name in EXCLUDED_FILES:
        logging.info(f"Skipping {rule_file_name} (excluded).")
        return None

    try:
        toml_dict = toml.loads(content)

        fields_to_extract = [
            "metadata.creation_date", "metadata.integration", "metadata.maturity",
            "metadata.updated_date", "rule.author", "rule.description", "rule.false_positives",
            "rule.from", "rule.index", "rule.language", "rule.license", "rule.name",
            "rule.references", "rule.risk_score", "rule.rule_id", "rule.severity", "rule.tags",
            "rule.timeline_id", "rule.timeline_title", "rule.timestamp_override", "rule.type",
            "rule.query", "rule.threat"
        ]

        flattened_dict = {field: extract_toml_value(toml_dict, field) for field in fields_to_extract}
        flattened_dict["GitHub Folder Location"] = os.path.dirname(item["path"])
        flattened_dict["GitHub File Name"] = rule_file_name

        return flattened_dict

    except toml.TomlDecodeError as e:
        logging.error(f"TOML decoding error in {rule_file_name}: {e}")
    except IndexError as e:
        logging.error(f"Index error in {rule_file_name}: {e}")
    except Exception as e:
        logging.error(f"Unexpected error parsing {rule_file_name}: {e}")
    
    return None


def extract_toml_value(toml_dict, field):
    """Extract the value from the TOML dictionary based on the field path."""
    keys = field.split('.')
    temp = toml_dict
    for key in keys:
        try:
            if isinstance(temp, dict) and key in temp:
                temp = temp[key]
            else:
                return None
        except IndexError:
            logging.warning(f"Index out of range when accessing '{field}'")
            return None
    return temp

def write_to_csv(data, repository):
    """Write parsed data to a CSV file."""
    
    if repository == "splunk":
        OUTPUT_CSV = f"splunk_rules_export_{CURRENT_DATE}.csv"
        fieldnames = [
            "GitHub Folder Location", "GitHub File Name", "Name", 
            "ID", "Version", "Date", "Author", "Status", "Type", 
            "Description", "Data Source", "Search", "How To Implement", 
            "Known False Positives", "Falsepositives", "References", 
            "Analytic Story", "Confidence", "Impact", "Risk Score", 
            "Message", "MITRE ATT&CK ID"
        ]
        
    elif repository == "sigmahq":
        OUTPUT_CSV = f"sigma_rules_export_{CURRENT_DATE}.csv"
        fieldnames = [
        "GitHub Folder Location", "GitHub File Name", "Title", "ID", "Status",
        "Description", "Date", "Modified", "Tags", "Product", "Category", "Service",
        "Author", "Detection", "Falsepositives", "Level"
        ]
        
    elif repository == "elastic" or repository == "elastic_bbr":
        OUTPUT_CSV = f"{repository}_rules_export_{CURRENT_DATE}.csv"
        fieldnames = [
        'GitHub File Name', 'GitHub Folder Location', "metadata.creation_date", "metadata.integration", 
        "metadata.maturity", "metadata.updated_date", "rule.author", "rule.description", 
        "rule.false_positives", "rule.from", "rule.index", "rule.language", "rule.license", "rule.name", 
        "rule.references", "rule.risk_score", "rule.rule_id", "rule.severity", "rule.tags", 
        "rule.timeline_id", "rule.timeline_title", "rule.timestamp_override", "rule.type", 
        "rule.query", "rule.threat"
        ]
        
    try:
        with open(OUTPUT_CSV, mode="w", newline="", encoding="utf-8") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        logging.info(f"CSV file '{OUTPUT_CSV}' created successfully.")
    except IOError as e:
        logging.error(f"Failed to write CSV: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Export Elastic, SigmaHQ or Splunk detection rule GitHub repositories to CSV")
    parser.add_argument(
        "-r", "--repositories", nargs='+', required=True,
        help="List of repositories to export: elastic, elastic_bbr, splunk, sigmahq"
    )
    args = parser.parse_args()
    
    main(args.repositories)