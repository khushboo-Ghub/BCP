# Input number of strings
T = int(input("Enter number of strings: "))

# Loop for each string
for _ in range(T):
    S = input("Enter a string: ")
    vowels = 0
    consonants = 0
    
    # Loop through each character in the string
    for char in S:
        if char.isalpha():  # Check if character is a letter
            if char.lower() in 'aeiou':
                vowels += 1
            else:
                consonants += 1
    
    # Print count of vowels and consonants
    print(vowels, consonants)