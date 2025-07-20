# Vowel Counter Script

# Function to count vowels in a given word
def count_vowels(word):
    vowels = "aeiouAEIOU"  # Vowels (both uppercase and lowercase)
    count = 0
    
    # Loop through each character in the word
    for char in word:
        if char in vowels:
            count += 1
    
    return count

# Input: Word to check
word = input("Enter a word to count the vowels: ")

# Count vowels in the word
vowel_count = count_vowels(word)

# Print the result
print(f"The number of vowels in the word '{word}' is: {vowel_count}")
