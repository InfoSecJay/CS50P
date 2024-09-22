import sys
import csv
from tabulate import tabulate

def main():
    check_args()
    try:
        csv_file = sys.argv[1] 
        print(convert_csv(csv_file))
    except FileNotFoundError:
        sys.exit("File does not exist")
    
def convert_csv(csv_file):
    
    with open(csv_file) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        csv_header = csv_reader.fieldnames
        csv_rows = [row.values() for row in csv_reader]
        return tabulate(csv_rows, headers=csv_header, tablefmt="grid")

def check_args():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
        
if __name__ == "__main__":
    main()