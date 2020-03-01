a=int(input())
arr=[0 for i in range(a+1)]
arr[1]=0
for i in range(2,a+1,1):
    arr[i]=arr[i-1]+1
    if i%2==0:
        arr[i]=min(arr[i],arr[int(i/2)]+1)
    if i%3==0:
        arr[i] = min(arr[i], arr[int(i / 3)] + 1)

print(arr[a])