import csv


# Takes CSV file and returns the headers and rows
def import_csv(filepath):
    # Initializations
    headers = []
    rows = []

    # Open CSV File
    with open(filepath, 'r') as _csv_file:
        csv_reader = csv.reader(_csv_file)

        # Receive the headers
        headers = next(csv_reader)

        # Receive the rows
        for row in csv_reader:
            rows.append(row)

    return headers, rows
