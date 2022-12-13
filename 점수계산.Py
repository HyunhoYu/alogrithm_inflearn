import sys
sys.stdin = open("input.txt", "rt")

len = int(input())
n_list = list(map(int,input().split()))

'''
for i in range(1,len):
    if n_list[i-1] >= 1 and n_list[i] == 1:
        n_list[i] = n_list[i-1] + 1

print(sum(n_list))


'''
cnt = 0
sum = 0
for x in n_list:
    if x == 1:
        cnt += 1
        sum += cnt
    else:
        cnt = 0

print(sum)
