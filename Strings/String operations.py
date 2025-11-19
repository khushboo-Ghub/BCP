# Input string
A = input("Enter the string: ")

# Step 1: Concatenate the string with itself
A = A + A

# Step 2: Delete all uppercase letters
A = ''.join([ch for ch in A if ch.islower()])

# Step 3: Replace each vowel with '#'
vowels = 'aeiou'
A = ''.join(['#' if ch in vowels else ch for ch in A])

# Print the resultant string
print(A)