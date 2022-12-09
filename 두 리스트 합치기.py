n = int(input())
lst = list(map(int,input().split()))
lst2 = []
ave = round(sum(lst)/len(lst))

min = 2147000000


for x in lst:
    dif = abs(ave - x)
    if dif < min:
        min = dif
        tmp = x
        lst2.append(x)
    elif dif == min:
        if x > tmp:
            lst2.append(x)
        
   


    

print(ave, lst.index(lst2[-1])+1)
