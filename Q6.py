# Q6 - Nested Data: A Railway Timetable

import time
import random

# Railway timetable with 5 trains
timetable = {
    "12601": {
        "name": "Chennai Express",
        "stops": [
            ("Chennai", "06:00", "06:10"),
            ("Vijayawada", "11:00", "11:05"),
            ("Hyderabad", "15:00", "15:10")
        ],
        "days": {"Monday", "Wednesday", "Friday"}
    },

    "12602": {
        "name": "Bangalore Express",
        "stops": [
            ("Chennai", "07:00", "07:15"),
            ("Katpadi", "09:00", "09:05"),
            ("Bangalore", "12:00", "12:10")
        ],
        "days": {"Tuesday", "Thursday", "Saturday"}
    },

    "12603": {
        "name": "Coimbatore Express",
        "stops": [
            ("Chennai", "08:00", "08:10"),
            ("Salem", "13:00", "13:05"),
            ("Coimbatore", "16:00", "16:10")
        ],
        "days": {"Monday", "Tuesday", "Friday"}
    },

    "12604": {
        "name": "Madurai Express",
        "stops": [
            ("Chennai", "09:00", "09:10"),
            ("Trichy", "14:00", "14:05"),
            ("Madurai", "17:00", "17:10")
        ],
        "days": {"Wednesday", "Thursday", "Sunday"}
    },

    "12605": {
        "name": "Mysore Express",
        "stops": [
            ("Chennai", "10:00", "10:10"),
            ("Katpadi", "12:00", "12:05"),
            ("Mysore", "17:00", "17:10")
        ],
        "days": {"Monday", "Thursday", "Saturday"}
    }
}

# Display complete timetable
print("RAILWAY TIMETABLE")

for train_no, details in timetable.items():

    print("\nTrain Number:", train_no)
    print("Train Name:", details["name"])
    print("Running Days:", sorted(details["days"]))

    for station, arrival, departure in details["stops"]:
        print(station, arrival, departure)


# Find trains at a particular station on a given day
def find_trains(station, day):

    result = []

    for train_no, details in timetable.items():

        if day not in details["days"]:
            continue

        for stop in details["stops"]:

            name, arrival, departure = stop

            if name.lower() == station.lower():

                result.append(
                    (train_no, details["name"], departure)
                )

    return sorted(result, key=lambda x: x[2])


station = input("\nEnter Station Name: ")
day = input("Enter Day: ").capitalize()

trains = find_trains(station, day)

print("\nAvailable Trains:")

if trains:
    for train in trains:
        print(train)
else:
    print("No trains available")


# Create station index
station_index = {}

for train_no, details in timetable.items():

    for station_name, arrival, departure in details["stops"]:

        station_index.setdefault(
            station_name.lower(), []
        ).append(train_no)


print("\nStation Index:")
print(station_index)


# Compare query without and with index
start = time.perf_counter()

for i in range(1000):
    find_trains("Chennai", "Monday")

normal_time = time.perf_counter() - start

start = time.perf_counter()

for i in range(1000):
    indexed_trains = station_index.get("chennai", [])

indexed_time = time.perf_counter() - start

print("\nQuery Performance:")
print("Without Index:", normal_time)
print("With Index:", indexed_time)


# Unknown station test
print("\nUnknown Station:")
print(find_trains("Mumbai", "Monday"))

# Train not running on the day
print("\nTrain Not Running:")
print(find_trains("Bangalore", "Monday"))