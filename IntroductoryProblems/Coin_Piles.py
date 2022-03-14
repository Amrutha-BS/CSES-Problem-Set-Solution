n=int(input())
s=[]
for i in range(n):
	s.append(list(map(int,input().split())))
for i in s:
    if sum(i)%3!=0 or i[0]>2*i[1] or i[1]>2*i[0]:
        print("NO")
    else:
        print("YES")