#06-03-2022 N0:1
n=int(input())
arr=list(map(int,input().split()))
maxi=0
s=0
for i in arr:
    if s+i<=0:
        maxi=max(maxi,s)
        s=0
    elif s+i<s:
        maxi=max(maxi,s)
        s=s+i
    else:
        s=s+i
maxi=max(maxi,s)
if maxi==0:
    maxi=max(arr)
print(maxi)
#8
#-1 3 -2 5 3 -5 2 2		
		
