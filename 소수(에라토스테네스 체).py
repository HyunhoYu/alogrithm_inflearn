import sys
sys.stdin = open("input.txt", "rt")

"""""
tc = int(input())

numbers = [0 for _ in range (tc+1)]

cnt = 0

for i in range (2, tc+1):
    if numbers[i] == 0:
        cnt += 1
        for j in range(i, tc+1, i):
            numbers[j] = 1

print(cnt)

"""""

n = int(input())

numbers = [i for i in range(1, n+1)]



for x in numbers:
    index = numbers.index(x)
    if x == 1:
        numbers[0] = 1
    elif x % 2 == 0 or x % 3 ==0:
        numbers[index] = 1
    else:
        numbers[index] = 0


print(numbers.count(0)+2)