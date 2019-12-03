N=int(input())
arr=list(map(int,input().split()))
temp=[]
temp.append(arr[0])

for i in range(len(arr)-1):
    temp.append(max(temp[i]+arr[i+1],arr[i]))
print(max(temp))