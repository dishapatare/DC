
import csv
from datetime import datetime
from collections import defaultdict

def map_function(filename):
    mapped = []
    with open(filename, "r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            try:
                date = row[0]
                max_temp = float(row[2])
                min_temp = float(row[3])
                year = datetime.strptime(date, "%Y-%m-%d").year
                mapped.append((year,(max_temp, min_temp, 1)))
            except:
                continue
    return mapped

def shuffle(mapped_data):
    shuffled = defaultdict(list)
    for year, values in mapped_data:
        shuffled[year].append(values)
    return shuffled

def reduce_function(shuffled_data):
    hottest_year = None
    coolest_year = None
    max_avg_temp = float("-inf")
    min_avg_temp = float("inf")

    for year, values in shuffled_data.items():
        count = sum(v[2] for v in values)
        max_avg = sum(v[0] for v in values) / count
        min_avg = sum(v[1] for v in values) / count

        if max_avg > max_avg_temp:
            max_avg_temp = max_avg
            hottest_year = year

        if min_avg < min_avg_temp:
            min_avg_temp = min_avg
            coolest_year = year

    return hottest_year, max_avg_temp, coolest_year, min_avg_temp

mapped = map_function("weather.csv")
shuffled = shuffle(mapped)
hottest_year, max_avg_temp, coolest_year, min_avg_temp = reduce_function(shuffled)

print(f"Hottest Year: {hottest_year} with avg max temperature: {max_avg_temp:.2f}°C")
print(f"Coolest Year: {coolest_year} with avg min temperature: {min_avg_temp:.2f}°C")

