n,s=list(map(int,input().split()))
arr=list(map(int,input().split()))
d={}
i,j,count=0,n-1,0
tracker=0
for i in arr:
    if d=={}:
        d[tracker]=[i]
    else:
        flag=0
        for j in d:
            if sum(d[j])+i<=s:
                flag=1
                d[j].append(i)
                break
        if flag==0:
           tracker+=1
           d[tracker]=[i]
#print(d)                
print(len(d))

#4 10
#4 8 6 1
#
#
#1 4 6 8
#10 100
#36 16 7 33 2 53 25 48 32 11