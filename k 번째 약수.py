import sys
sys.stdin = open("input.txt", "rt")

n, k = map(int,input().split())

void_list = []

for i in range (1, n+1):
    if n % i == 0:
        void_list.append(i)

if len(void_list) < k:
    print(-1)
else:
    print(void_list[k-1])
    
    

