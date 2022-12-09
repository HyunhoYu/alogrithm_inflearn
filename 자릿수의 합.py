import sys
sys.stdin = open("input.txt", "rt")

tc = int(input())
digit = list(map(int,input().split()))

rst_list = []

sum = 0
for x in digit:
    stfy = str(x)
    for i in range(len(stfy)):
        sum += int(stfy[i])
    rst_list.append(sum)
    sum = 0 

max = 0 
for x in rst_list:
    if x > max:
        max = x
print(digit[rst_list.index(max)])
        

