# reverse string using recursion
def rev(s):
    if s == "":
        return ""
    return rev(s[1:]) + s[0]

s = input()
print(rev(s))