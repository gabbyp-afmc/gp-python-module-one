import csv
from datetime import date

from trips import Trip

COLUMNS = ['destination', 'start_date', 'end_date', 
           'flights_cost', 'hotel_cost_per_day', 'other_cost_per_day']

def read_file(input_file):
    trips = []
    skipped_row_errors = []
    missing_cols = []
    
    with open(input_file) as file:
        reader = csv.DictReader(file)
            
        #check if empty input file
        if reader.fieldnames is None:
            raise ValueError(input_file + "is an empty file")

        #check if an expected column is missing
        for column in COLUMNS:
            if column not in reader.fieldnames:
                missing_cols.append(column)
        if missing_cols:
            raise ValueError(f"Missing column(s): {', '.join(missing_cols)}")

        #create trips objects from input file
        for row in reader:
            try:
                trip = Trip(get_string(row, "destination"),
                            get_date(row, "start_date"),
                            get_date(row, "end_date"),
                            get_float(row, "flights_cost"),
                            get_float(row, "hotel_cost_per_day"),
                            get_float(row, "other_cost_per_day"))
                trips.append(trip)
            except ValueError as err:
                skipped_row_errors.append(f"Skipped row {reader.line_num}: {err}")

        if not trips and not skipped_row_errors:
            raise ValueError(input_file + "has no row data")
        return trips, skipped_row_errors

def get_string(row, column):
    value = (row[column] or "").strip()
    if not value:
        raise ValueError(f"Column '{column}' is blank")
    return value

def get_date(row, column):
    value = get_string(row, column)
    try:
        return date.fromisoformat(value)
    except ValueError:
        raise ValueError(f"Column '{column}' has invalid value '{value}', expected format of YYYY-MM-DD")

def get_float(row, column):
    value = get_string(row, column)
    try:
        return float(value)
    except ValueError:
        raise ValueError(f"Column '{column}' has invalid value '{value}', expected number")