import sys



sys.stdin = open("input.txt", "rt")

n = int(input())
score_list = list(map(int,input().split()))

average = round(sum(score_list)/n)
min = 2147000000

for x in score_list:
    dev = abs(x - average)
    dev2 = abs(min-average)
    if dev < dev2:
        min = x
    elif dev == dev2:
        if x > min:
            min = x

print(average, score_list.index(min)+1)
        


