n=int(input())
if n%4==1 or n%4==2:
    print("NO")
elif n%4==3:
    print("YES")
    print(n//2)
    print(3,end=" ")
    for i in range(4,n,4):
        print(i,i+3,end=" ")
    print()
    print((n//2)+1)
    print(1,2,end=" ")
    for i in range(4,n,4):
        print(i+1,i+2,end=" ")    
else:
    print("YES")
    print(n//2)
    for i in range(2,n,4):
        print(i,i+1,end=" ")
    print()
    print(n//2)
    for i in range(1,n,4):
        print(i,i+3,end=" ")
    
        