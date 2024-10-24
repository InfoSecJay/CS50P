import sys
import csv

def main():
    check_args()
    input_csv = sys.argv[1] 
    output_csv = sys.argv[2]
    process_csv(input_csv, output_csv)


def process_csv(input_csv, output_csv):
    try:
        with open(input_csv, 'r', newline='') as in_file:
            reader = csv.DictReader(in_file)
            new_list = []
            for row in reader:
                last,first = row['name'].split(", ")
                house = row['house']
                new_list.append({"first": first, "last": last, "house": house})
                
            with open(output_csv, 'w', newline='') as out_file:
                writer = csv.DictWriter(out_file, fieldnames = ["first", "last", "house"])
                writer.writeheader()
                for row in new_list:
                    writer.writerow(row)
    except FileNotFoundError:
        sys.exit("Could not find file")


def check_args():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if not (sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv")):
        sys.exit("Not a CSV file")

if __name__ == "__main__":
    main()