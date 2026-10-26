# Vacation Cost Calculator

A command-line tool that reads a CSV of planned trips, calculates each trip's
length and total cost, and writes the results to a new CSV. Invalid rows are skipped with a message naming the row,
column, and value.

## Requirements

Python 3. No extra libraries needed.

## How to run

```bash
python3 main.py INPUT.csv OUTPUT.csv
```

Example:

```bash
python3 main.py vacationValid.csv output.csv
```

## Input format

The input CSV must have these columns:

| Column | Example |
|---|---|
| destination | London |
| start_date | 2027-04-12 |
| end_date | 2027-04-19 |
| flights_cost | 600 |
| hotel_cost_per_day | 300 |
| other_cost_per_day | 150 |

Total cost = flights + (hotel + other) × number of days.

## Error handling

- Missing columns, an empty file, or a file with no rows stop the program with a message.
- Rows with blank values, invalid numbers or dates, negative costs, or an end
  date before the start date are skipped, and the program says which row and
  column caused it.

Try the sample files `vacationInvalidCost.csv`, `vacationInvalidDateStr.csv`,
and `vacationNegCost.csv` to see this.

## Project structure

| File | Purpose |
|---|---|
| main.py | Handles command-line arguments and error messages |
| trips.py | The Trip class: calculations and validation rules |
| file_reader.py | Reads the CSV and turns rows into Trip objects |
| file_writer.py | Writes the results CSV |
