# Simple Cipher Script

# Function to shift each letter in a word by 1 position in the alphabet
def simple_cipher(word):
    ciphered_word = ""
    
    for char in word:
        # Check if the character is a letter
        if char.isalpha():
            # Shift the letter by 1 position
            if char.lower() == 'z':
                ciphered_word += 'a' if char.islower() else 'A'
            else:
                ciphered_word += chr(ord(char) + 1) if char.islower() else chr(ord(char) + 1).upper()
        else:
            # If it's not a letter, add the character as it is
            ciphered_word += char
            
    return ciphered_word

# Input: Word to apply the cipher
word = input("Enter a word: ")

# Apply the cipher and display the result
ciphered = simple_cipher(word)
print(f"Ciphered word: {ciphered}")
