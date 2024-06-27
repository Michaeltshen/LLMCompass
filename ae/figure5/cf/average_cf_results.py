import csv
from collections import defaultdict

grouped_data = defaultdict(lambda: ([]))

csv_file = 'cf_gpu_results.csv'
output_csv_file = 'cf_gpu_average_results.csv'

with open(csv_file, mode='r', newline='') as file:
    reader = csv.reader(file)
    next(reader)  
    for row in reader:
        key = (int(row[0]), int(row[1]))
        value = float(row[2])  
        grouped_data[key].append(value)

averages_list = []
for key, value in grouped_data.items():
    avg_value = sum(value) / len(value) if value else 0
    averages_list.append([key[0], key[1], avg_value])


with open(output_csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['M', 'N', 'GElements/s'])
    writer.writerows(averages_list)
