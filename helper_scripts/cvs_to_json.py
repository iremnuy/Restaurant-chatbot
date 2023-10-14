import csv
import json

csv_file = '/Users/wbagger/Documents/talabat_menuitem_all.csv'
json_file = '/Users/wbagger/Documents/talabat_menuitem_all.json'

data = []

# Read the CSV file and convert it to a list of dictionaries
with open(csv_file, 'r') as csvf:
    csv_reader = csv.DictReader(csvf)
    for row in csv_reader:
        data.append(row)

# Write the data to a JSON file
with open(json_file, 'w') as jsonf:
    jsonf.write(json.dumps(data, indent=4))

print(f'CSV file "{csv_file}" has been converted to JSON in "{json_file}".')
