n = int(input())
count = 0

for i in range(n):
    marks, att = map(int,input().split())
    if marks >= 75 and att >=80:
        count +=1
       
   
print(count)


n = int(input())

eligible_count = 0

for _ in range(n):
    marks, attendance = map(int, input().split())
    if marks >= 75 and attendance >= 80:
        eligible_count += 1
print(eligible_count)