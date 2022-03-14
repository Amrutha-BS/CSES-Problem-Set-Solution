#06-03-2022 N0:6
n=int(input())
arr=list(map(int,input().split()))
s=[]
for i in range(n):
    while(len(s)>0 and s[-1][0]>=arr[i]):
	    s.pop()
    if len(s)==0:
	    print(0,end=" ")
    else:
        print(s[-1][1],end=" ")
    s.append([arr[i],i+1])
#8
#2 5 1 4 8 3 2 5
