import pytest
from count_vowel_consonant_pairs import count_vowel_consonant_pairs


# Test a large input with 1,000 vowels followed by 1,000 consonants
def test_large_input():
    vowels = "a" * 1000  # String of 1000 'a' vowels
    consonants = "b" * 1000  # String of 1000 'b' consonants
    large_text = vowels + consonants  # Concatenate them
    assert count_vowel_consonant_pairs(large_text) == 1  # Only one transition


# Test a string of 1,000 alternating vowel-consonant pairs
def test_large_alternating_input():
    alternating_text = "ab" * 1000  # 'ab' repeated 1000 times
    assert count_vowel_consonant_pairs(alternating_text) == 1000  # 1000 valid pairs


import random
import string


# Test a large string with random characters
def test_random_large_input():
    # Generate a random string of 10,000 characters (letters, numbers, special characters)
    random_text = "".join(random.choices(string.ascii_letters + string.digits + "!@#$%", k=10000))
    result = count_vowel_consonant_pairs(random_text)

    # Ensure the function runs without crashing and returns an integer
    assert isinstance(result, int)
