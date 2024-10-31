# def count_word_frequency(C:\\Users\ndevr\\OneDrive\\Desktop\\PYTHON\\file.txt):
#     """Counts the frequency of words in the specified file."""
#     try:
#         with open(C:\Users\ndevr\OneDrive\Desktop\PYTHON\file.txt, 'r') as file:
#             words = file.read().lower().split()
#         word_frequency = {}
#         for word in words:
#             word_frequency[word] = word_frequency.get(word, 0) + 1
#         return word_frequency
#     except FileNotFoundError:
#         print(f"The file {C:\Users\ndevr\OneDrive\Desktop\PYTHON\file.txt} does not exist.")
#         return None
import re

def count_word_frequency(file_path):
    """Counts the frequency of words in the specified file."""
    try:
        with open(file_path, 'r') as file:
            text = file.read().lower()
        words = re.findall(r'\b\w+\b', text)
        word_frequency = {}
        for word in words:
            word_frequency[word] = word_frequency.get(word, 0) + 1
        return word_frequency
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
        return None

file_path = 'C:\\Users\\ndevr\\OneDrive\\Desktop\\PYTHON\\file.txt'
word_frequency = count_word_frequency(file_path)

if word_frequency:
    for word, frequency in word_frequency.items():
        print(f"{word}: {frequency}")