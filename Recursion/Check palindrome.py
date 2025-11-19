# check palindrome using recursion
def isPal(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return isPal(s[1:-1])

s = input()
if isPal(s):
    print("Palindrome")
else:
    print("Not Palindrome")