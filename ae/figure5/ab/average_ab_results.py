import csv
from collections import defaultdict

grouped_data = defaultdict(lambda: ([], []))

csv_file = 'ab_gpu_results.csv'
output_csv_file = 'ab_gpu_average_results.csv'

with open(csv_file, mode='r', newline='') as file:
    reader = csv.reader(file)
    next(reader)  
    for row in reader:
        key = (int(row[0]), int(row[1]), int(row[2]))
        value1 = float(row[3][:-2]) 
        value2 = float(row[4][:-6])  
        grouped_data[key][0].append(value1)
        grouped_data[key][1].append(value2)

averages_list = []
for key, values in grouped_data.items():
    avg_value1 = sum(values[0]) / len(values[0]) if values[0] else 0
    avg_value2 = sum(values[1]) / len(values[1]) if values[1] else 0
    averages_list.append([key[0], key[1], key[2], avg_value1, avg_value2])


with open(output_csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['M', 'N', 'K', 'Latency(ms)', 'TFlops'])
    writer.writerows(averages_list)
