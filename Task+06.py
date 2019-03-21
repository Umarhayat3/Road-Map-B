import csv
result = [field for field in csv.DictReader(open('abc.csv', newline='',errors='ignore'))]
print(result)
