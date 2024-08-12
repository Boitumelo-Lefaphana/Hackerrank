# Read the number of words
n = int(input())

# Initialize a dictionary to store word counts and a list for order
word_counts = {}
word_order = []

# Read words and count occurrences
for _ in range(n):
    word = input().strip()
print(' '.join(str(word_counts[word]) for word in word_order))