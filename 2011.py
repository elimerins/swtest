a = list(map(int, input()))
l = len(a)
dp = [0] * (l+1)
#dp[l]을 출력하려면 l+1개 인덱스가 필요함.

dp[0] = 1
for i in range(1, l + 1):
    if 1 <= a[i-1] and a[i-1] <= 9:
        dp[i] += dp[i - 1]
    if i == 1:
        continue
    cur2 = a[i - 2] * 10 + a[i - 1]
    if cur2 >= 10 and cur2 <= 26:
        dp[i] += dp[i - 2]
print(dp[l] % 1000000)
