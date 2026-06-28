import math

try:
    # Take input sentence
    sentence = input("Enter a sentence: ")

    if sentence.strip() == "":
        print("Empty sentence entered!")
    else:
        # Convert sentence into words and store unique words in set
        words = sentence.lower().split()
        unique_words = set(words)

        # Sort unique words
        sorted_words = sorted(unique_words)

        print("\nUnique words:", unique_words)
        print("Sorted unique words:", sorted_words)

        # Count unique words
        count = len(unique_words)

        # Power using math module
        result = math.pow(count, 2)

        print("Total unique words:", count)
        print("Square of unique words count:", result)

except Exception as e:
    print("Error occurred:", e)