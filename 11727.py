N = int(input())

arr = [1, 3]
for i in range(2, N):
    arr.append(arr[i - 1] + 2 * arr[i - 2])

print(arr[N-1] % 10007)
