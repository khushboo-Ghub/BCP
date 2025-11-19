#Q.3 read N, print reverse of n


# Q.1 read N, print sum of digits in N.

# N = int(input("Enter your number"))

# S = 0
# while(N>0):

#     digit = N % 10
#     N = N//10
#     S += digit



#Q.2 read N and a single digit "D", add "D" back to N


# n = int(input("Enter your number: "))

# ans = 0
# while(n>0):
#     digit = n % 10
#     n = n//10
#     ans = ans * 10 + digit

# print(ans)





# # 1
# N = int(input("Enter a positive integer N: "))
# for i in range(1, N+1):
#     print(i, end=' ')


# # 2
# N = int(input("Enter a positive integer N: "))
# for i in range(N, 0, -1):
#     print(i, end=' ')


# # 3
# N = int(input("Enter a positive integer N: "))
# for i in range(2, N+1, 2):
#     print(i, end=' ')


# # 4
# N = int(input("Enter a positive integer N: "))
# for i in range(1, N+1, 2):
#     print(i, end=' ')


# # 5
# N = int(input("Enter a positive integer N: "))
# sum = 0
# for i in range(1, N+1):
#     sum += i
# print(sum)


# # 6
# A = int(input("Enter an integer A: "))
# sum = 0
# for i in range(2, A+1, 2):
#     sum += i
# print(sum)


# # 7
# A = int(input("Enter an integer A: "))
# sum = 0
# for i in range(1, A+1, 2):
#     sum += i
# print(sum)


# # 8
# N = int(input("Enter an integer N: "))
# count = 0
# temp = N
# while temp != 0:
#     temp = temp // 10
#     count += 1
# print(count)


# # 9
# N = int(input("Enter an integer N: "))
# sum_digits = 0
# temp = N
# while temp != 0:
#     digit = temp % 10
#     sum_digits += digit
#     temp = temp // 10
# print(sum_digits)


# # 10
# A = int(input("Enter an integer A: "))
# original = A
# reverse = 0
# while A > 0:
#     digit = A % 10
#     reverse = reverse * 10 + digit
#     A = A // 10
# if original == reverse:
#     print("Yes")
# else:
#     print("No")


# # 11
# A = int(input("Enter an integer A: "))
# for i in range(1, 11):
#     print(f"{A} * {i} = {A*i}")


# # 12
# A = int(input("Enter integer A: "))
# B = int(input("Enter integer B: "))
# result = 1
# for _ in range(B):
#     result *= A
# print(result)



# This is only for practice codes of python


# The range method / Function is used to generate a range of integers


# # Generate even numbers from 0 to 8
# for i in range(0, 12, 2):
#     print(i)


# for i in range(0, 12, 2):
#     print(i*i, end= " ")


# for i in range(1, N + 1):
#     print(i)




# for i in range(1,N+1,2):
#     print(i, end= " ")


# for i in range(a):
#     ans = ans*b
#     print(ans.end=" ")



# for i in range(100):
#     print(i.end= " ")
#     if(i % 3 == 0):
#         if(i % 3 == 0):
#             continue
#         print(i)





# # *******
# m = 5
# for i in range(m):
#     print("*", end= " ")
# print("")
# print("")



# # *
# # *
# # *
# # *
# # *
# a = 5
# for i in range(a):
#     print("*")
# print("")


# n = 5
# for i in range(n):
#     print("* " * n)
# print("")



# b = 5
# for i in range(5):
#     print("*"*(i+1))


# rows = 5
# for i in range(1, rows + 1):
#     # Left stars
#     print("*" * i, end="")
    
#     # Spaces
#     spaces = (rows - i) * 2   # adjust space multiplier
#     print(" " * spaces, end="")
    
#     # Right stars
#     print("*" * i)



# # 1
# # 1*3*
# # 1*3*5
# # 1*3*5*

# for i in range(10):
#     for j in range(i):
#         if(j%2==0):
#             print("*",end=" ")
#         else:
#             print(j,end=" ")
#     print("")



# # practice at day of a bunk

# name = "Utkarsh Tripathi"
# for i in name:
#     print(i)
#     if(i =="t"):
#         print("This is unique")
        


# for i in range(1, 8400000):
#     print(i)





# practice at day of (07-09-2025)


# 1 Print numbers from 1 to 10.

# for i in range(1, 11):
#     print(i)

# 2.	Print the multiplication table of 5.
# for i in range(1, 11):
#     print(f" 5 ❌ {i} = {i * 5}")

# 3. Print all even numbers between 1 and 20.

# for i in range(1, 21):
#     if i % 2 == 0:
#         print(i)

# print("...")

# for j in range(1, 21):
#     if j % 2 != 0:
#         print(j)
    
    
# Print the sum of numbers from 1 to 100.
# n = 0
# for i in range(1, 101):
#     n = n + i
#     print("Sum = ", n)

    

# Print each character of a string using a loop.
# l = "Utkarsh In IIT Vrindavan"
# for i in l:
#     print(i, end="")

# (Using GPT)
# text = "Harivansh"

# for char in text:
#     print(char)



# 6. Print numbers from 10 to 1 (reverse order).

# n = 10
# while n >= 1:
#     print(n)
#     n -= 1


# Find the factorial of a number using a while loop.
# nhi ker rha ho abhi me

# 8. Print the first 10 natural numbers using while loop.

# n = 1
# while n <= 10:
#     print(n)
#     n += 1





# ..............




#  9. Keep asking the user for input until they enter "stop".
# u = int(input("Enter your number"))
# while u != "Stop":
#     if u != "Stop":
#         print("You entered: ", u )
# print("end")


# user_input = ""

# while user_input != "stop":
#     user_input = input("Enter something (eg: type 'stop' to end): ")
#     if user_input != "stop":
#         print("You entered:", user_input)

# print("Program ended.")



# 10. Print the digits of a number separately (e.g., 123 → 1, 2, 3).
# ..............


# 4
# Write a program to print all odd numbers from 1 to N, where you have to take N as input
# from user.
# Input:- N = 10Output:- 1 3 5 7 9

# n = int(input("Value of N"))
# i = 1

# while i <= n: 
#     if i % 2 != 0:
#         print(i)
#     i += 1 





# n = 5
# for i in range(1, n+1):
#     if i % 2 == 0:
#         print("1*3*"[:i])
#     else:
#         seq = [str(x) for x in range(1, 2*i, 2)]
#         print("*".join(seq))


# n = 5
# for i in range(n):
#     print("*" + "_ "*(n-i-1) + "_*")








# _ _ _ _ *  
# _ _ _ *  *  
# _ _ *  *  *  
# _ *  *  *  *  
# *  *  *  *  *  
# n = 5
# for i in range(1, n+1):
#     print("_ "*(n-i) + "*  " * i)







# *  *  *  *  *  
# _ *  *  *  *  
# _ _ *  *  *  
# _ _ _ *  *  
# _ _ _ _ *  
# n = 5
# for i in range(n, 0, -1):
#     print("_ "*(n-i) + "*  " * i)





# n = 5
# for i in range(n):
#     print("*"*(n-i) + "  "*(i) + "*"*(n-i))



# n = 5
# for i in range(1, n+1):
#     print("*"*i + "  "*(n-i) + "*"*i)



# n = 5
# for i in range(n):
#     print("ð"*(n-i) + "  "*(i) + "ð"*(n-i))
# for i in range(n):
#     print("ð"*(i+1) + "  "*(n-i-1) + "ð"*(i+1))



# n = 4
# for i in range(n, 0, -1):       # loop from 4 → 1
#     row = ""                    # empty string for each row
#     for j in range(1, i+1):     # print numbers from 1 → i
#         row += str(j) + " "
#     print(row)


# n = 4        # total rows
# num = 1      # starting number

# for i in range(1, n+1):         # loop for rows
#     for j in range(1, i+1):     # loop for printing numbers in row
#         print(num, end=" ")     # print number
#         num += 1                # increase number
#     print()                     # move to next line



# n = 5
# # Increasing part
# for i in range(1, n+1):
#     print("*" * i)

# # Decreasing part
# for i in range(n-1, 0, -1):
#     print("*" * i)



# Give an array and a target number find number of occurence of target number given array

# Type 1
arr = [1, 2, 3, 2, 4, 2, 5]
target = 2
count = 0
for num in arr:
    if num == target:
        count += 1

print("Number of occurrences:", count)

# Type 2
arr = [1, 2, 3, 2 ,5 , 4, 2, 5, 4, 5, 6, 5]
target = 2
p = 5
occurrence = arr.count(target)
occ = arr.count(p)
print("Number of occurrences:", occurrence)
print("Number of occ:", occ)



# given an array and increment number generate a new array contanining all the value of the original array with the increment number

# arr = list(map(int, input("Enter").split()))
# ans = -float("inm")
# for i in arr:
#     if ans < i:
#         ans = i
# print(ans)



