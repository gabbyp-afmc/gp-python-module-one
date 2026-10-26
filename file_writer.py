import csv

def write_file(trips, output_file):
    with open(output_file, "w") as file:
        writer = csv.DictWriter(file, fieldnames=["destination","duration_days","total_cost"])
        writer.writeheader()
        for trip in trips:
            writer.writerow({"destination":trip.destination,"duration_days":trip.duration_days,
                             "total_cost":trip.total_cost})