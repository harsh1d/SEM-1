filename = 'example.txt'  # Replace with your text file name


def count_lines_and_unique_words(filepath):
  unique_words = set()
  lines_count = 0

  with open(filepath, 'r') as file:
    for line in file:
      lines_count += 1
      words = line.split()
      unique_words.update(words)

  return lines_count, len(unique_words)


# Example usage:
lines, unique_words = count_lines_and_unique_words(filename)
print(f'Number of lines: {lines}')
print(f'Number of unique words: {unique_words}')
