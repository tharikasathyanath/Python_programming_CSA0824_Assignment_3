# Q7 - Design a Contact-Merging Program from First Principles

import re
import time
import random

# Contact details from different phones
phone1 = [
    {
        "name": "Dr. Ravi",
        "phone": "+91 98400 12345",
        "email": "ravi@gmail.com"
    },
    {
        "name": "Priya",
        "phone": "9876543210",
        "email": "priya@gmail.com"
    },
    {
        "name": "Arun",
        "phone": "9123456789",
        "email": "arun@gmail.com"
    }
]

phone2 = [
    {
        "name": "ravi kumar",
        "phone": "9840012345",
        "email": "ravi@yahoo.com"
    },
    {
        "name": "Priya",
        "phone": "+91 9876543210",
        "email": "priya@gmail.com"
    },
    {
        "name": "Divya",
        "phone": "9988776655",
        "email": "divya@gmail.com"
    }
]

sim_contacts = [
    {
        "name": "Ravi",
        "phone": "98400-12345",
        "email": "ravi@gmail.com"
    },
    {
        "name": "Kumar",
        "phone": "",
        "email": "kumar@gmail.com"
    }
]


# Normalize phone number
def normalize_phone(phone):

    digits = re.sub(r"\D", "", phone)

    if len(digits) == 12 and digits.startswith("91"):
        digits = digits[2:]

    return digits


# Normalize name
def normalize_name(name):

    return " ".join(name.lower().strip().split())


# Merge contacts
def merge_contacts(contact_lists):

    merged = {}

    for contacts in contact_lists:

        for contact in contacts:

            name = contact.get("name", "").strip()
            phone = normalize_phone(contact.get("phone", ""))
            email = contact.get("email", "").strip().lower()

            # Use normalized phone as key
            if phone:

                if phone not in merged:

                    merged[phone] = {
                        "names": set(),
                        "numbers": set(),
                        "emails": set()
                    }

                if name:
                    merged[phone]["names"].add(name)

                merged[phone]["numbers"].add(phone)

                if email:
                    merged[phone]["emails"].add(email)

            # Store contacts without phone separately
            else:

                key = "NO_PHONE:" + normalize_name(name)

                if key not in merged:

                    merged[key] = {
                        "names": set(),
                        "numbers": set(),
                        "emails": set()
                    }

                if name:
                    merged[key]["names"].add(name)

                if email:
                    merged[key]["emails"].add(email)

    return merged


# Combine all contact lists
all_contacts = [phone1, phone2, sim_contacts]

# Measure execution time
start = time.perf_counter()

result = merge_contacts(all_contacts)

end = time.perf_counter()

print("MERGED CONTACTS")
print("------------------------")

for key, details in result.items():

    print("\nContact:", key)

    print("Names:", sorted(details["names"]))

    print("Phone Numbers:", sorted(details["numbers"]))

    print("Email Addresses:", sorted(details["emails"]))


print("\nTotal Unique Contacts:", len(result))

print("Execution Time:", end - start, "seconds")


# Generate test contacts
def generate_contacts(size):

    contacts = []

    for i in range(size):

        contacts.append({
            "name": "Person " + str(i),
            "phone": str(9000000000 + i),
            "email": "person" + str(i) + "@gmail.com"
        })

    return contacts


# Performance test
print("\nPERFORMANCE TEST")

for size in [1000, 100000]:

    test_data = generate_contacts(size)

    start = time.perf_counter()

    merged_data = merge_contacts([test_data])

    elapsed = time.perf_counter() - start

    print("\nNumber of Contacts:", size)
    print("Unique Contacts:", len(merged_data))
    print("Execution Time:", elapsed, "seconds")


# Small test for duplicate verification
test_contacts = [
    {"name": "Ravi", "phone": "+91 98400 12345",
     "email": "ravi@gmail.com"},

    {"name": "ravi kumar", "phone": "9840012345",
     "email": "ravi@yahoo.com"}
]

test_result = merge_contacts([test_contacts])

print("\nDUPLICATE TEST")
print(test_result)

# Missing field test
missing_contacts = [
    {"name": "Kumar", "phone": "", "email": "kumar@gmail.com"},
    {"name": "Priya", "phone": "9876543210", "email": ""}
]

print("\nMISSING FIELD TEST")
print(merge_contacts([missing_contacts]))