def count_vowel_consonant_pairs(text):
    """
    Counts the number of occurrences where a vowel is
    immediately followed by a consonant in the input string.

    Args:
        text (str): The input string to analyze.

    Returns:
        int: Count of vowel-consonant pairs.

    Raises:
        TypeError: If the input is not a string.
    """
    if not isinstance(text, str):  # Ensure the input is a string
        raise TypeError("Input must be a string")

    vowels = "aeiouAEIOU"  # Define vowels (both uppercase and lowercase)
    count = 0  # Initialize count variable

    # Iterate through the string up to the second-to-last character
    for i in range(len(text) - 1):
        # Check if the current character is a vowel and the next is a consonant
        if text[i] in vowels and text[i + 1].isalpha() and text[i + 1] not in vowels:
            count += 1  # Increment count if a vowel-consonant pair is found

    return count  # Return the total count
