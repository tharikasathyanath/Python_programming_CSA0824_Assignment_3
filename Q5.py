# Q5 - List Comprehension: Cleaning Sensor Readings

import random
import time
import sys

readings = [
    4, 5, 7, 9, 55, -60, 3, 6, 8, 10,
    2, 4, 51, -55, 5
]

# Method 1: Using for loop and append
def using_loop(data):

    valid = []

    for temperature in data:
        if -50 <= temperature <= 50:
            valid.append(temperature)

    fahrenheit = []

    for temperature in valid:
        fahrenheit.append((temperature * 9/5) + 32)

    return valid, fahrenheit


# Method 2: Using list comprehension
def using_comprehension(data):

    valid = [
        temperature for temperature in data
        if -50 <= temperature <= 50
    ]

    fahrenheit = [
        (temperature * 9/5) + 32
        for temperature in valid
    ]

    return valid, fahrenheit


# Method 3: Using map and filter
def using_map_filter(data):

    valid = list(filter(
        lambda x: -50 <= x <= 50,
        data
    ))

    fahrenheit = list(map(
        lambda x: (x * 9/5) + 32,
        valid
    ))

    return valid, fahrenheit


# Display results
valid1, fahrenheit1 = using_loop(readings)

valid2, fahrenheit2 = using_comprehension(readings)

valid3, fahrenheit3 = using_map_filter(readings)

print("Original Readings:")
print(readings)

print("\nValid Celsius Readings:")
print(valid2)

print("\nFahrenheit Readings:")
print(fahrenheit2)

# Alarm minutes outside 2 to 8 degree Celsius
alarm_minutes = [
    minute
    for minute, temperature in enumerate(readings, start=1)
    if -50 <= temperature <= 50
    and not (2 <= temperature <= 8)
]

print("\nAlarm Minutes:")
print(alarm_minutes)

# Dictionary comprehension
temperature_dict = {
    minute: temperature
    for minute, temperature in enumerate(readings, start=1)
    if -50 <= temperature <= 50
}

print("\nTemperature Dictionary:")
print(temperature_dict)

# Set comprehension
temperature_set = {
    temperature
    for temperature in readings
    if -50 <= temperature <= 50
}

print("\nTemperature Set:")
print(temperature_set)

# Verify all methods
print("\nVerification:")
print(valid1 == valid2 == valid3)
print(fahrenheit1 == fahrenheit2 == fahrenheit3)

# Performance comparison
print("\nPerformance Comparison")

for size in [10000, 100000, 1000000]:

    data = [
        random.uniform(-60, 60)
        for i in range(size)
    ]

    start = time.perf_counter()
    using_loop(data)
    loop_time = time.perf_counter() - start

    start = time.perf_counter()
    using_comprehension(data)
    comprehension_time = time.perf_counter() - start

    start = time.perf_counter()
    using_map_filter(data)
    map_time = time.perf_counter() - start

    print("\nReadings:", size)
    print("Loop Time:", loop_time)
    print("Comprehension Time:", comprehension_time)
    print("Map and Filter Time:", map_time)

# Memory comparison
valid_list = [x for x in readings if -50 <= x <= 50]

generator = (x for x in readings if -50 <= x <= 50)

print("\nList Memory:", sys.getsizeof(valid_list))
print("Generator Memory:", sys.getsizeof(generator))

# All valid and all invalid tests
print("\nAll Valid:", using_comprehension([2, 3, 4, 5]))
print("All Invalid:", using_comprehension([60, 70, -80]))