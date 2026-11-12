# Q1 - Lists and Slicing: Daily Rainfall Records

import random
import time

# Generate 365 daily rainfall readings
readings = [random.randint(0, 100) for i in range(365)]

# Display weekly totals using slicing
weekly_totals = []

for i in range(0, len(readings), 7):
    weekly_totals.append(sum(readings[i:i+7]))

print("Weekly Rainfall Totals:")
print(weekly_totals)

# Maximum and minimum rainfall
if readings:
    print("\nMaximum Rainfall:", max(readings))
    print("Maximum Position:", readings.index(max(readings)))

    print("Minimum Rainfall:", min(readings))
    print("Minimum Position:", readings.index(min(readings)))

# 7-day moving average using normal method
def naive_average(data):
    averages = []

    for i in range(len(data) - 6):
        averages.append(sum(data[i:i+7]) / 7)

    return averages


# 7-day moving average using running sum
def running_average(data):
    averages = []

    if len(data) < 7:
        return averages

    current_sum = sum(data[:7])
    averages.append(current_sum / 7)

    for i in range(7, len(data)):
        current_sum += data[i] - data[i-7]
        averages.append(current_sum / 7)

    return averages


print("\n7-Day Moving Average:")
print(running_average(readings))

# Dry days
dry_days = [i+1 for i in range(len(readings)) if readings[i] == 0]

print("\nDry Days:")
print(dry_days)

# Slicing examples
print("\nReadings[7:14]:", readings[7:14])
print("Readings[-7:]:", readings[-7:])
print("Readings[::7]:", readings[::7])

# Experimental investigation
print("\nPerformance Comparison")

for size in [365, 36500, 365000]:

    data = [random.randint(0, 100) for i in range(size)]

    start = time.perf_counter()
    naive_average(data)
    naive_time = time.perf_counter() - start

    start = time.perf_counter()
    running_average(data)
    running_time = time.perf_counter() - start

    print("\nReadings:", size)
    print("Naive Time:", naive_time)
    print("Running Sum Time:", running_time)

# Edge cases
print("\nEmpty List:", running_average([]))
print("Short List:", running_average([10, 20, 30]))