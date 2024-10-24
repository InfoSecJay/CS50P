import os
import csv
import requests
import yaml
import toml
import base64
import argparse
from datetime import datetime
from dotenv import load_dotenv
from typing import List, Dict, Any, Optional

# Load environment variables
load_dotenv()

# Constants
GITHUB_TOKEN = os.getenv("github_token")
HEADERS = {"Authorization": f"token {GITHUB_TOKEN}"}
CURRENT_DATE = datetime.now().strftime("%d_%m_%Y")

# Repository URLs
SIGMAHQ_URL = "https://api.github.com/repos/SigmaHQ/sigma/contents/rules"
ELASTIC_URL = "https://api.github.com/repos/elastic/detection-rules/contents/rules"

# Excluded files for SigmaHQ
SIGMA_EXCLUDED_FILES = {
    "driver_load_win_mal_drivers.yml",
    "driver_load_win_mal_drivers_names.yml",
    "driver_load_win_vuln_drivers.yml",
    "driver_load_win_vuln_drivers_names.yml",
}

# Excluded files for SigmaHQ
ELASTIC_EXCLUDED_FILES = {
}

# Fields to extract from Elastic TOML files
ELASTIC_FIELDS = [
    "metadata.creation_date", "metadata.integration", "metadata.maturity",
    "metadata.min_stack_comments", "metadata.min_stack_version", "metadata.updated_date",
    "rule.author", "rule.description", "rule.false_positives", "rule.from",
    "rule.index", "rule.language", "rule.license", "rule.name", "rule.note",
    "rule.references", "rule.risk_score", "rule.rule_id", "rule.severity",
    "rule.tags", "rule.timestamp_override", "rule.type", "rule.query"
]

def create_session() -> requests.Session:
    """Create a reusable HTTP session with default headers."""
    session = requests.Session()
    session.headers.update(HEADERS)
    return session

def fetch_content(url: str, session: requests.Session) -> Optional[str]:
    """Fetch content from a given URL using the provided session."""
    try:
        response = session.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def write_to_csv(data: List[Dict[str, Any]], filename: str, fieldnames: List[str]) -> None:
    """Write collected data to a CSV file."""
    if not data:
        print("No data found.")
        return

    os.makedirs(os.path.dirname(filename), exist_ok=True)  # Ensure folder exists
    with open(filename, mode="w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

    print(f"CSV file '{filename}' created successfully.")

def parse_yaml_file(item: Dict[str, Any], session: requests.Session) -> Optional[Dict[str, Any]]:
    """Parse a YAML file if it's not in the excluded list."""
    if item["name"] in SIGMA_EXCLUDED_FILES:
        print(f"Skipping {item['name']} (excluded).")
        return None

    yaml_content = fetch_content(item["download_url"], session)
    if not yaml_content:
        return None

    parsed = yaml.safe_load(yaml_content)
    logsource = parsed.get("logsource", {})

    return {
        "GitHub Folder Location": os.path.dirname(item["path"]),
        "GitHub File Name": item["name"],
        "Title": parsed.get("title", ""),
        "ID": parsed.get("id", ""),
        "Status": parsed.get("status", ""),
        "Description": parsed.get("description", ""),
        "Date": parsed.get("date", ""),
        "Modified": parsed.get("modified", ""),
        "Tags": parsed.get("tags", ""),
        "Product": logsource.get("product", ""),
        "Category": logsource.get("category", ""),
        "Author": parsed.get("author", ""),
        "Detection": parsed.get("detection", ""),
        "Falsepositives": parsed.get("falsepositives", ""),
        "Level": parsed.get("level", ""),
    }

def scrape_sigma_files(url: str, session: requests.Session) -> List[Dict[str, Any]]:
    """Fetch and parse YAML files from the SigmaHQ repository."""
    response = session.get(url)
    response.raise_for_status()
    data = response.json()
    results = []

    for item in data:
        if item["type"] == "file" and item["name"].endswith(".yml"):
            parsed = parse_yaml_file(item, session)
            if parsed:
                results.append(parsed)
        elif item["type"] == "dir":
            results.extend(scrape_sigma_files(item["url"], session))

    return results

def parse_toml_file(item: Dict[str, Any], session: requests.Session) -> Optional[Dict[str, Any]]:
    """Parse a TOML file and extract relevant fields."""
    content = fetch_content(item["url"], session)
    if not content:
        return None

    try:
        decoded_content = base64.b64decode(content).decode("utf-8")
        parsed = toml.loads(decoded_content)
        flattened = {}

        for field in ELASTIC_FIELDS:
            keys = field.split('.')
            temp = parsed
            for key in keys:
                temp = temp.get(key) if isinstance(temp, dict) else None
                if temp is None:
                    break
            flattened[field] = temp

        flattened["GitHub Folder Location"] = os.path.dirname(item["path"]).split("/rules/", 1)[-1]
        flattened["GitHub File Name"] = item["name"]
        return flattened

    except Exception as e:
        print(f"Error parsing {item['name']}: {e}")
        return None

def scrape_elastic_files(url: str, session: requests.Session) -> List[Dict[str, Any]]:
    """Fetch and parse TOML files from the Elastic repository."""
    response = session.get(url)
    response.raise_for_status()
    data = response.json()
    results = []

    for item in data:
        if item["type"] == "file" and item["name"].endswith(".toml"):
            parsed = parse_toml_file(item, session)
            if parsed:
                results.append(parsed)
        elif item["type"] == "dir":
            results.extend(scrape_elastic_files(item["url"], session))

    return results

def main(repository: str) -> None:
    """Main entry point. Export the selected repository to CSV."""
    session = create_session()

    if repository == "sigmahq":
        data = scrape_sigma_files(SIGMAHQ_URL, session)
        filename = f"sigma_rules_export_{CURRENT_DATE}.csv"
        fieldnames = [
            "GitHub Folder Location", "GitHub File Name", "Title", "ID", "Status",
            "Description", "Date", "Modified", "Tags", "Product", "Category", 
            "Author", "Detection", "Falsepositives", "Level"
        ]
    elif repository == "elastic":
        data = 2(ELASTIC_URL, session)
        filename = f"elastic_detection_rules_export_{CURRENT_DATE}.csv"
        fieldnames = ["GitHub Folder Location", "GitHub File Name"] + ELASTIC_FIELDS
    else:
        print("Invalid repository. Choose 'sigmahq' or 'elastic'.")
        return

    write_to_csv(data, filename, fieldnames)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Export a detection rule repository to CSV.")
    parser.add_argument(
        "-r", "--repository", type=str, required=True,
        help="Repository to export: 'sigmahq' or 'elastic'."
    )
    args = parser.parse_args()
    print(f"Exporting: {args.repository}")
    main(args.repository)
