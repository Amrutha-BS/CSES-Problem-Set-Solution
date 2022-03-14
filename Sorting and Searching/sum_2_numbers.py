#06-03-2022 N0:3
n,s=list(map(int,input().split()))
a=list(map(int,input().split()))
i=0
j=len(a)-1
flag=0
arr=[i for i in a]
arr.sort()
while(i<j):
    if arr[i]+arr[j]==s:    
        #print(arr[i],arr[j],i,j)
        flag=1
        #print(i+1,j+1)
        break
    elif arr[i]+arr[j]<s:
	    i+=1
    else:
        j-=1
if flag==1:
    index1=a.index(arr[i])
    a[index1]=arr[i]-99999
    index2=a.index(arr[j])
    print(index1+1,index2+1)
elif flag==0:
	print("IMPOSSIBLE")
