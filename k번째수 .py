import sys
sys.stdin = open("input.txt", "rt")

tc = int(input())

tool_list = []
rst = 0
for i in range(tc):
    condition = list(map(int,input().split()))
    problem = list(map(int,input().split()))
    tool_list.append(problem[condition[1]-1 : condition[2]])
    tool_list[0].sort()
    rst = tool_list[0][condition[3]-1]
    print("#%d %d" %(i+1,rst))
    tool_list.clear()
  




