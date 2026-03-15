import random

# List of quotes
quotes = [
    {"quote": "Keep going, you are closer than you think.", "author": "Unknown"},
    {"quote": "Believe you can and you're halfway there.", "author": "Theodore Roosevelt"},
    {"quote": "It always seems impossible until it's done.", "author": "Nelson Mandela"},
    {"quote": "Don't watch the clock, do what it does. Keep going.", "author": "Sam Levenson"},
    {"quote": "Success is not final, failure is not fatal.", "author": "Winston Churchill"},
]

def get_random_quote():
    return random.choice(quotes)

def get_quote_by_author(author):
    results = [q for q in quotes if q["author"].lower() == author.lower()]
    if not results:
        return None
    return random.choice(results)

def get_all_quotes():
    return quotes

def count_quotes():
    return len(quotes)
