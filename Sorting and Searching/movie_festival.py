n=int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))
count=0
arr.sort(key=lambda x:x[1])
current_end_time=0
for start,end in arr:
    if start>=current_end_time:
        count+=1
        current_end_time=end
print(count)
        
 