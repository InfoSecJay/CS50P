import sys
import csv

def main():
    check_args()
    input_csv = sys.argv[1] 
    output_csv = sys.argv[2]
    process_csv(input_csv, output_csv)


def process_csv(input_csv, output_csv):
    
    with open(input_csv, 'r', newline='') as in_file:
        reader = csv.DictReader(in_file)
        
        with open(output_csv, 'w', newline='') as out_file:
            writer = csv.DictWriter(out_file, fieldnames = reader.fieldnames)
            writer.writeheader()
            for row in reader:
                last, first = row['name'].split(', ')
                writer.writerow(row)









def check_args():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if not (sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv")):
        sys.exit("Not a CSV file")

if __name__ == "__main__":
    main()