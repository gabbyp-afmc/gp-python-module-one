import sys

from file_reader import read_file
from file_writer import write_file

def main():
    if len(sys.argv) == 3:
        if sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv") and sys.argv[1] != sys.argv[2]:
            try:
                input_file = sys.argv[1]
                output_file = sys.argv[2]
                trips, skipped_row_errors = read_file(input_file)
    
                for skip in skipped_row_errors:
                    print(skip)
        
                write_file(trips, output_file)
                for trip in trips:
                    print(trip)
                print(f"Wrote {len(trips)} trips to {output_file}")
    
            except FileNotFoundError:
                sys.exit("Could not read " + input_file)
            except (ValueError, KeyError) as err:
                sys.exit(f"Invalid data: {err}")
        else:
            sys.exit("Both files must be CSVs and different")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        sys.exit("Too few command-line arguments")

if __name__ == "__main__":
    main()
