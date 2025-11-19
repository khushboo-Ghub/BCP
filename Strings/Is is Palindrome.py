# Input number of strings
T = input("Enter number of strings: ")

# Loop through each string
for _ in range(T):
    S = input("Enter a string: ")
    
    # Check if string is equal to its reverse
    if S == S[::-1]:
        print(1)
    else:
        print(0)