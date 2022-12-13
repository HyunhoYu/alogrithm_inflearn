"https://velog.io/@rapid97/Python-인프런-알고리즘"     # <<<<<코드 설명은 여기서!!!!

import sys
sys.stdin = open("input.txt", "rt")

"""

prime_number = [0 for _ in range(1, 100001)]

for i in range (2, len(prime_number)):
    if prime_number[i] == 0:
        for j in range(i+i, len(prime_number), i):
            prime_number[j] = 1
prime_number[1] = 1



case = int(input())
numbers = list(map(int,input().split()))

sub_string_list = []
sub_string = ""
for i in range(case):
    strfy = str(numbers[i])
    for j in range(len(strfy)-1, -1, -1):
        sub_string += strfy[j]
    sub_string_list.append(sub_string)
    sub_string = ""



for x in sub_string_list:
    x = int(x)
    if prime_number[x] == 0:
        print(x, end = ' ')


"""

def reverse(x):
    rst = 0
    while x > 0:
        t = x % 10
        rst = rst * 10 + t
        x = x // 10
    return rst

def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x//2 + 1):
        if x % i == 0:
            return False
    else:
        return True




n = int(input())
numbers = list(map(int,input().split()))

for x in numbers:
    tmp = reverse(x)
    if isPrime(tmp):
        print(tmp, end= ' ')







   






