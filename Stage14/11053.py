N = int(input())
A = list(map(int, input().split()))
dp = [1] * N

for i in range(len(A)):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(dp)
print(max(dp))
