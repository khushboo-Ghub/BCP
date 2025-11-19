# Input string
A = input("Enter the string: ")

# Split the string into words
words = A.split()

# Reverse the order of words
reversed_words = words[::-1]

# Join the words back into a string
result = ' '.join(reversed_words)

# Print the result
print(result)