# Input string
A = input("Enter the string: ")

# Split the string into words
words = A.split()

# Reverse each word individually
reversed_words = [word[::-1] for word in words]

# Join the reversed words back into a string
result = ' '.join(reversed_words)

# Print the result
print(result)