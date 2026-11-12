# Q4 - Sets: Elective Registration Clash Detection

import time

ai_elective = {
    "192311001",
    "192311004",
    "192311007",
    "192311009"
}

iot_elective = {
    "192311002",
    "192311004",
    "192311009",
    "192311010"
}

all_students = {
    f"1923110{i:02d}" for i in range(1, 11)
}

# Set operations
both = ai_elective & iot_elective

exactly_one = ai_elective ^ iot_elective

neither = all_students - (ai_elective | iot_elective)

print("clash      :", sorted(both))
print("exactly one:", sorted(exactly_one))
print("neither    :", sorted(neither))

# Using set methods
both_method = ai_elective.intersection(iot_elective)

exactly_one_method = ai_elective.symmetric_difference(iot_elective)

neither_method = all_students.difference(
    ai_elective.union(iot_elective)
)

print("\nUsing Set Methods")

print("clash      :", sorted(both_method))
print("exactly one:", sorted(exactly_one_method))
print("neither    :", sorted(neither_method))

print("\nResults Same:")
print(both == both_method)
print(exactly_one == exactly_one_method)
print(neither == neither_method)

# Remove duplicate registrations
registrations = [
    "192311001",
    "192311004",
    "192311004",
    "192311007"
]

unique_registrations = set(registrations)

print("\nUnique Registrations:")
print(sorted(unique_registrations))

# Performance comparison
print("\nMembership Performance")

for size in [10000, 100000, 1000000]:

    numbers = [str(i) for i in range(size)]
    number_set = set(numbers)

    search_value = str(size - 1)

    start = time.perf_counter()
    result1 = search_value in numbers
    list_time = time.perf_counter() - start

    start = time.perf_counter()
    result2 = search_value in number_set
    set_time = time.perf_counter() - start

    print("\nSize:", size)
    print("List Search Time:", list_time)
    print("Set Search Time:", set_time)

# Empty elective test
empty = set()

print("\nEmpty Elective:", sorted(empty & ai_elective))

# Identical elective test
print("Identical Electives:", sorted(ai_elective & ai_elective))

# Verify with nested loops
common = []

for student in ai_elective:
    for other in iot_elective:
        if student == other:
            common.append(student)

print("\nNested Loop Result:", sorted(common))
print("Set Result:", sorted(both))