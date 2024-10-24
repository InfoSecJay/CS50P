import os
import csv
import requests
import yaml
from datetime import datetime
from dotenv import load_dotenv
from requests.exceptions import RequestException
import logging
from time import sleep
import argparse


# Load environment variables
load_dotenv()

# GitHub repository URL and token
SPLUNK_GITHUB_API_URL = "https://api.github.com/repos/splunk/security_content/contents/detections/network"
SIGMAHQ_GITHUB_API_URL = "https://api.github.com/repos/SigmaHQ/sigma/contents/rules/web"
GITHUB_TOKEN = os.getenv("github_token")

# Get the current date
CURRENT_DATE = datetime.now().strftime("%d_%m_%Y")

# Output files (CSV and log)

LOG_FILE = f"rules_export_log_{CURRENT_DATE}.log"

# List of files to exclude
EXCLUDED_FILES = {
}

# Configure logging to both console and log file
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


def main(repository: str) -> None:
    """Main function to fetch, parse, and export YAML data."""
    
    if not GITHUB_TOKEN:
        logging.error("GitHub token not found. Please check your .env file.")
        return
    
    if repository == "splunk":
        print("Exporting: " + repository)
        
        yaml_data = scrape_yaml_files(SPLUNK_GITHUB_API_URL, repository)

        if yaml_data:
            write_to_csv(yaml_data, repository)
        else:
            logging.warning("No YAML files were fetched.")
    
    elif repository == "sigmahq":
        print("Exporting: " + repository)
        
        yaml_data = scrape_yaml_files(SIGMAHQ_GITHUB_API_URL, repository)

        if yaml_data:
            write_to_csv(yaml_data, repository)
        else:
            logging.warning("No YAML files were fetched.")
    else:
        print("Invalid repository. Choose 'sigmahq' or 'elastic'.")
        return



def fetch_yaml_content(url):
    """Fetch YAML content from a given URL."""
    try:
        response = session.get(url)
        response.raise_for_status()
        return yaml.safe_load(response.text)
    except RequestException as e:
        logging.error(f"Error fetching {url}: {e}")
        return None


def scrape_yaml_files(url, repository):
    """Recursively fetch and parse YAML files from the GitHub repository."""
    try:
        response = session.get(url)
        response.raise_for_status()
        data = response.json()
    except RequestException as e:
        logging.error(f"Failed to fetch data from {url}: {e}")
        return []

    yaml_data = []

    for item in data:
        if item["type"] == "file" and item["name"].endswith(".yml"):
            
            rule_folder_location = os.path.dirname(item["path"]) # Get rule folder path
            rule_file_name = item["name"]
            
            if rule_file_name in EXCLUDED_FILES:
                logging.info(f"Skipping {rule_file_name} (excluded).")
                continue
            
            yaml_url = item["download_url"]          # Example: "https://api.github.com/repos/SigmaHQ/sigma/contents/rules/web/product/apache"
            yaml_content = fetch_yaml_content(yaml_url)
            
            if yaml_content and repository == "splunk":
                logging.info(f"Parsing {rule_file_name}...")

                tags = yaml_content.get("tags", {})
                yaml_data.append({
                    "GitHub Folder Location": rule_folder_location,
                    "GitHub File Name": rule_file_name,
                    "Name": yaml_content.get("name", ""),
                    "ID": yaml_content.get("id", ""),
                    "Version": yaml_content.get("version", ""),
                    "Date": yaml_content.get("date", ""),                    
                    "Author": yaml_content.get("author", ""),
                    "Status": yaml_content.get("status", ""),
                    "Type": yaml_content.get("type", ""),
                    "Description": yaml_content.get("description", ""),
                    "Data Source": yaml_content.get("data_source", ""),
                    "Search": yaml_content.get("search", ""),
                    "How To Implement": yaml_content.get("how_to_implement", ""),
                    "Known False Positives": yaml_content.get("known_false_positives", ""),
                    "Falsepositives": yaml_content.get("falsepositives", ""),
                    "References": yaml_content.get("references", ""),
                    "Analytic Story": tags.get("analytic_story", ""),
                    "Confidence": tags.get("confidence", ""),
                    "Impact": tags.get("impact", ""),
                    "Risk Score": tags.get("risk_score", ""),
                    "Message": tags.get("impact", ""),
                    "MITRE ATT&CK ID": tags.get("impact", "")
                })
            elif yaml_content and repository == "sigmahq":
                logging.info(f"Parsing {rule_file_name}...")

                logsource = yaml_content.get("logsource", {})
                yaml_data.append({
                    "GitHub Folder Location": rule_folder_location,
                    "GitHub File Name": rule_file_name,
                    "Title": yaml_content.get("title", ""),
                    "ID": yaml_content.get("id", ""),
                    "Status": yaml_content.get("status", ""),
                    "Description": yaml_content.get("description", ""),
                    "Date": yaml_content.get("date", ""),
                    "Modified": yaml_content.get("modified", ""),
                    "Tags": yaml_content.get("tags", ""),
                    "Product": logsource.get("product", ""),
                    "Category": logsource.get("category", ""),
                    "Service": logsource.get("service", ""),
                    "Author": yaml_content.get("author", ""),
                    "Detection": yaml_content.get("detection", ""),
                    "Falsepositives": yaml_content.get("falsepositives", ""),
                    "Level": yaml_content.get("level", ""),
                })
            else:
                logging.warning(f"Skipping {rule_file_name} due to fetch error.")

        elif item["type"] == "dir":
            logging.info(f"Entering directory: {item['name']}")
            yaml_data.extend(scrape_yaml_files(item["url"], repository))

    return yaml_data




def write_to_csv(data, repository):
    """Write parsed YAML data to a CSV file."""
    
    if repository == "splunk":
        fieldnames = [
            "GitHub Folder Location", "GitHub File Name", "Name", 
            "ID", "Version", "Date", "Author", "Status", "Type", 
            "Description", "Data Source", "Search", "How To Implement", 
            "Known False Positives", "Falsepositives", "References", 
            "Analytic Story", "Confidence", "Impact", "Risk Score", 
            "Message", "MITRE ATT&CK ID"
        ]
        OUTPUT_CSV = f"splunk_rules_export_{CURRENT_DATE}.csv"
    else:
        fieldnames = [
        "GitHub Folder Location", "GitHub File Name", "Title", "ID", "Status",
        "Description", "Date", "Modified", "Tags", "Product", "Category", "Service",
        "Author", "Detection", "Falsepositives", "Level"
        ]
        
        OUTPUT_CSV = f"sigma_rules_export_{CURRENT_DATE}.csv"
    try:
        with open(OUTPUT_CSV, mode="w", newline="", encoding="utf-8") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        logging.info(f"CSV file '{OUTPUT_CSV}' created successfully.")
    except IOError as e:
        logging.error(f"Failed to write CSV: {e}")




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Export a detection rule repository to csv")
    parser.add_argument("-r", "--repository", required=True, help="repository to export: elastic or sigmahq", type=str)
    args = parser.parse_args()
    main(args.repository)
