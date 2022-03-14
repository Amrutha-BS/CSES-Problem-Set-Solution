n=int(input())
val=1
count=2
num=1000000007
while(n>0):
    if n%2:
        val=val*count
    count=count*count
    n=n>>1
print(val%num)