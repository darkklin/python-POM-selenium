import csv
import os

def getCVSData(filename):
    # create an empty list to store rows
    rows = []
    # open the CSV file
    dirname = os.path.dirname(__file__)
    dataFile = open(os.path.join(dirname, filename))
    # dataFile = open(os.path.dirname(os.path.realpath(filename)))

    # create a CSV Reader from CSV file
    reader = csv.reader(dataFile)
    # skip the header
    next(reader)
    # add rows from reader to list
    for row in reader:
        rows.append(row)
    return rows