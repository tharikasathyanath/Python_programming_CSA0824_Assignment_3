# Q3 - Dictionaries: Farmer Helpline Complaint Analysis

import random
import string
import time
from collections import Counter

calls = [
    "seeds not received seeds delayed",
    "fertiliser price high",
    "seeds price high subsidy not received"
]

STOP = {"not", "high"}


# Count word frequencies
def frequencies(texts, stop):
    counts = {}

    for text in texts:
        words = text.lower().translate(
            str.maketrans("", "", string.punctuation)
        ).split()

        for word in words:
            if word not in stop:
                counts[word] = counts.get(word, 0) + 1

    return counts


# Find top k words
def top(counts, k):
    return sorted(
        counts.items(),
        key=lambda item: (-item[1], item[0])
    )[:k]


print("Word Frequencies:")
print(frequencies(calls, STOP))

print("\nTop 3 Words:")
print(top(frequencies(calls, STOP), 3))

# Group complaints by district
complaints = [
    ("Chennai", "Seeds not received"),
    ("Madurai", "Fertiliser price high"),
    ("Chennai", "Water problem"),
    ("Salem", "Crop disease"),
    ("Madurai", "Seeds delayed")
]

district_data = {}

for district, complaint in complaints:
    district_data.setdefault(district, []).append(complaint)

print("\nComplaints By District:")

for district, complaint_list in district_data.items():
    print(district, ":", complaint_list)

# Generate test data
print("\nPerformance Comparison")

for size in [1000, 10000, 100000]:

    data = [
        " ".join(random.choices(
            ["seeds", "water", "price", "fertiliser", "crop"],
            k=10
        ))
        for i in range(size)
    ]

    start = time.perf_counter()
    result = frequencies(data, STOP)
    dictionary_time = time.perf_counter() - start

    words = " ".join(data).split()

    start = time.perf_counter()
    unique_words = set(words)

    list_counts = {
        word: words.count(word)
        for word in unique_words
    }

    list_time = time.perf_counter() - start

    start = time.perf_counter()
    counter_result = Counter(words)
    counter_time = time.perf_counter() - start

    print("\nComplaints:", size)
    print("Dictionary Time:", dictionary_time)
    print("List Count Time:", list_time)
    print("Counter Time:", counter_time)

# Empty text test
print("\nEmpty Text:", frequencies([""], STOP))

# Uppercase and lowercase test
print("Case Test:", frequencies(
    ["SEEDS seeds Seeds"],
    STOP
))

# Punctuation test
print("Punctuation Test:", frequencies(
    ["Seeds, seeds! price."],
    STOP
))