import sys
sys.stdin = open("input.txt", "rt")

case = int(input())

tool_list = []


rst = 0
for _ in range(case):
    dice = list(map(int,input().split()))
    if dice.count(dice[0]) == 3:
        rst = dice[0] * 1000 + 10000
    else:
        for i in range(3):
            if dice.count(dice[i]) == 2:
                rst = dice[i] * 100 + 1000
            else:
                dice.sort()
                rst = dice[2] * 100
    tool_list.append(rst)
    rst = 0

tool_list.sort()
print(tool_list[case-1])
        
    
            
            
    