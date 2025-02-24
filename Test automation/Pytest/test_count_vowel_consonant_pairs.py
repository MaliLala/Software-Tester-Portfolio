import pytest
from count_vowel_consonant_pairs import count_vowel_consonant_pairs

# Parameterized test cases for different input scenarios
@pytest.mark.parametrize("input_text, expected", [
    ("hello", 1),  # 'e' -> 'l' is a vowel-consonant pair
    ("banana", 3),  # 'a' -> 'n' occurs three times
    ("AEIOUbc", 5),  # All vowels followed by 'b' are valid pairs
    ("", 0),  # Empty string has no pairs
    ("12345", 0),  # No letters, so no pairs
    ("PyThOn", 1),  # 'o' -> 'n' is the only valid pair
    ("a!e@i#o$u%", 0)  # Special characters interrupt valid pairs
])
def test_count_vowel_consonant_pairs(input_text, expected):
    assert count_vowel_consonant_pairs(input_text) == expected

# Additional edge case tests
@pytest.mark.parametrize("input_text, expected", [
    ("", 0),  # Empty string test
    ("a!e@i#o$u%", 0),  # Vowels separated by special characters
    ("12345", 0),  # Only numbers, no valid pairs
    ("a", 0),  # Single vowel, no valid pairs
    ("b", 0),  # Single consonant, no valid pairs
    ("a1e2i3o4u", 0)  # Vowels interrupted by numbers
])
def test_edge_cases(input_text, expected):
    assert count_vowel_consonant_pairs(input_text) == expected

# Negative tests for invalid input types
@pytest.mark.parametrize("invalid_input", [
    None,  # None type should raise TypeError
    12345,  # Integer input should raise TypeError
    ["hello"],  # List input should raise TypeError
    {"text": "hi"}  # Dictionary input should raise TypeError
])
def test_invalid_inputs(invalid_input):
    with pytest.raises(TypeError):
        count_vowel_consonant_pairs(invalid_input)  # Expect a TypeError
