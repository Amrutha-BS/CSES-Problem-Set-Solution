def backtrack(l,index,n):
	if index==n:
		ans.append(''.join(l))
	else:
		for i in range(index,n+1):
			l[index],l[i]=l[i],l[index]
			backtrack(l,index+1,n)
			l[index],l[i]=l[i],l[index]
s=input()
n=len(s)-1
l=list(s)
ans=[]
backtrack(l,0,n)
ans=list(set(ans))
ans.sort()
print(len(ans))
for i in ans:
    print(i)
