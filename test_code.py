import csv

with open ("attack_log.csv", "r") as f:
    csvReader = csv.reader(f)
    for row in csvReader:
        print(csvReader.line_num)
