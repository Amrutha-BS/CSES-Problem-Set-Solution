n=int(input())
arr=[]
arrival=[]
leave=[]
for i in range(n):
    arr=list(map(int,input().split()))
    arrival.append(arr[0])
    leave.append(arr[1])
arrival.sort()
leave.sort()
maxi,current=0,0
i,j=0,0
while i<n and j<n:
    if arrival[i]<leave[j]:
        current+=1
        i+=1
    else:
        current-=1
        j+=1
    if maxi<current:
       maxi=current
print(maxi)
    