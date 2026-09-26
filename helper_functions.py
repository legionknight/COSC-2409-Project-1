# helper_functions.py

# Function 1: generate_greeting
# Given an hour of the day, return an appropriate greeting message.
# - 5 <= hour < 12: "Good morning!"
# - 12 <= hour < 18: "Good afternoon!"
# - 18 <= hour <= 22: "Good evening!"
# - Otherwise: "Hello!"
def generate_greeting(hour):
    if 5 < hour < 12:
        greeting = "Good morning!"
    elif 12 < hour < 18:
        greeting = "Good afternoon!"
    elif 18 < hour < 22:
        greeting = "Good evening"
    else:
        greeting = "Hello!"
    return greeting


# Function 2: calculate_average
# Given a list of numbers, return the average.
# If the list is empty, return None.
def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    if len(numbers) > 0:
        return average
    else:
        return None


# Function 3: categorize_numbers
# Given a list of numbers, categorize them as "odd" or "even".
# Return a dictionary with two keys: 'odd' and 'even'.
# Each key should have a list of corresponding numbers.
def categorize_numbers(numbers):
    categorized = {
    "even": [],
    "odd": []
    }
    for i in numbers:
        if i % 2 != 0:
            categorized["odd"].append(i)
        else:
            categorized["even"].append(i)
    return categorized


# Function 4: count_word_frequency
# Given a list of words, return a dictionary with the frequency of each word.
def count_word_frequency(words):
    word_frequency = {}
    for a in words:
        word_frequency[a] = word_frequency.get(a,0) + 1
    return word_frequency


# Function 5: find_max_in_dict
# Given a dictionary, find and return the key with the highest value.
def find_max_in_dict(data):
    max_key = max(data, key=data.get)
    return max_key
