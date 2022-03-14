s=input()
e=""
count,m=1,1
for i in s:
	if i!=e:
		e=i
		count=1
	else:
		count+=1
		m=max(count,m)
print(m)