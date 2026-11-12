# Q2 - Tuples, Mutability and Copying

import copy
import sys
import time

rows, cols = 3, 4

# Incorrect grid
bad = [[0] * cols] * rows
bad[0][1] = 7

# Correct grid using list comprehension
good = [[0 for j in range(cols)] for i in range(rows)]
good[0][1] = 7

print("bad :", bad)
print("good:", good)

print(bad[0] is bad[1], good[0] is good[1])

# Tuples as dictionary keys
stops = {
    (13.0827, 80.2707): "Chennai Central",
    (13.0418, 80.2341): "T. Nagar"
}

print(stops[(13.0418, 80.2341)])

# Tuple unpacking
print("\nTuple Unpacking:")

for latitude, longitude in stops:
    print("Latitude:", latitude, "Longitude:", longitude)

# Aliasing
original = [10, 20, 30]
alias = original

alias.append(40)

print("\nAliasing:")
print("Original:", original)
print("Alias:", alias)

# Shallow copy
shallow = copy.copy(original)
shallow.append(50)

print("\nShallow Copy:")
print("Original:", original)
print("Shallow:", shallow)

# List slicing copy
slice_copy = original[:]
slice_copy.append(60)

print("\nSlicing Copy:")
print(slice_copy)

# Deep copy
nested = [[1, 2], [3, 4]]
deep = copy.deepcopy(nested)

deep[0][0] = 100

print("\nDeep Copy:")
print("Original:", nested)
print("Deep Copy:", deep)

# Demonstrate nested shallow copy
shallow_nested = copy.copy(nested)
shallow_nested[0][1] = 200

print("\nNested Shallow Copy:")
print("Original:", nested)
print("Shallow:", shallow_nested)

# List inside tuple
t = ([10, 20], 30)
t[0].append(40)

print("\nList Inside Tuple:", t)

# Memory comparison
values = list(range(1000000))
tuple_values = tuple(values)

print("\nMemory of List:", sys.getsizeof(values))
print("Memory of Tuple:", sys.getsizeof(tuple_values))

# Creation and indexing time
start = time.perf_counter()
a = list(range(1000000))
print("\nList Creation Time:", time.perf_counter() - start)

start = time.perf_counter()
b = tuple(range(1000000))
print("Tuple Creation Time:", time.perf_counter() - start)

start = time.perf_counter()
x = a[500000]
print("List Indexing Time:", time.perf_counter() - start)

start = time.perf_counter()
y = b[500000]
print("Tuple Indexing Time:", time.perf_counter() - start)

# List cannot be dictionary key
try:
    test = {[13.0418, 80.2341]: "T Nagar"}
except TypeError as e:
    print("\nError:", e)