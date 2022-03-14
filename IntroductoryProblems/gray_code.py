n=int(input())
def generate_code(n):
    if n<=0:
        return ["0"]
    elif n==1:
        return ["0","1"]
    else:
        recAns = generate_code(n-1)
        mainAns=[]
        for i in recAns:
            mainAns.append("0"+i)
        n=len(recAns)
        for i in range(n):
            mainAns.append("1"+recAns[n-i-1])
        return mainAns
ans=generate_code(n)
for i in ans:
     print(i)