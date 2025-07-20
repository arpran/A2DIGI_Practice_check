# Word Reverser Script

# Function to reverse individual words in a sentence
def reverse_words(sentence):
    # Split the sentence into words
    words = sentence.split()
    
    # Reverse each word in the list
    reversed_words = [word[::-1] for word in words]
    
    # Join the reversed words back into a sentence
    reversed_sentence = " ".join(reversed_words)
    
    return reversed_sentence

# Input: Sentence to reverse words
sentence = input("Enter a sentence: ")

# Reverse the words and display the result
result = reverse_words(sentence)
print(f"Reversed words sentence: {result}")
