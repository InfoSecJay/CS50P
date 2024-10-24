import os
import csv
import requests
import yaml
from datetime import datetime
from dotenv import load_dotenv
from requests.exceptions import RequestException
import logging
from time import sleep

# Load environment variables
load_dotenv()

# GitHub repository URL and token
GITHUB_API_URL = "https://api.github.com/repos/SigmaHQ/sigma/contents/rules/web"
GITHUB_TOKEN = os.getenv("github_token")

# Get the current date
CURRENT_DATE = datetime.now().strftime("%d_%m_%Y")

# Output files (CSV and log)
OUTPUT_CSV = f"sigma_rules_export_{CURRENT_DATE}.csv"
LOG_FILE = f"sigma_rules_log_{CURRENT_DATE}.log"

# List of files to exclude
EXCLUDED_FILES = {
    "driver_load_win_mal_drivers.yml",
    "driver_load_win_mal_drivers_names.yml",
    "driver_load_win_vuln_drivers.yml",
    "driver_load_win_vuln_drivers_names.yml",
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


def fetch_yaml_content(url):
    """Fetch YAML content from a given URL."""
    try:
        response = session.get(url)
        response.raise_for_status()
        return yaml.safe_load(response.text)
    except RequestException as e:
        logging.error(f"Error fetching {url}: {e}")
        return None


def scrape_yaml_files(url):
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

            if yaml_content:
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
                logging.warning(f"Skipping {yaml_file} due to fetch error.")

        elif item["type"] == "dir":
            logging.info(f"Entering directory: {item['name']}")
            yaml_data.extend(scrape_yaml_files(item["url"]))

    return yaml_data


def write_to_csv(data):
    """Write parsed YAML data to a CSV file."""
    fieldnames = [
        "GitHub Folder Location", "GitHub File Name", "Title", "ID", "Status",
        "Description", "Date", "Modified", "Tags", "Product", "Category", "Service",
        "Author", "Detection", "Falsepositives", "Level"
    ]

    try:
        with open(OUTPUT_CSV, mode="w", newline="", encoding="utf-8") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        logging.info(f"CSV file '{OUTPUT_CSV}' created successfully.")
    except IOError as e:
        logging.error(f"Failed to write CSV: {e}")


def main():
    """Main function to fetch, parse, and export YAML data."""
    if not GITHUB_TOKEN:
        logging.error("GitHub token not found. Please check your .env file.")
        return

    yaml_data = scrape_yaml_files(GITHUB_API_URL)

    if yaml_data:
        write_to_csv(yaml_data)
    else:
        logging.warning("No YAML files were fetched.")


if __name__ == "__main__":
    main()
