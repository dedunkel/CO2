#누적 합 1단계 11659번
'''
import sys
input=sys.stdin.readline

n, m=map(int, input().split())

num=list(map(int, input().split()))

arr=[0]
for k in range(1, n+1):
    arr.append(arr[k-1]+num[k-1])
for _ in range(m):
    i, j=map(int, input().split())
    print(arr[j]-arr[i-1])
'''

#누적 합 2단계 2559번
'''
import sys
input=sys.stdin.readline

n, k=map(int, input().split())

num=list(map(int, input().split()))

arr=[]
arr.append(sum(num[:k]))
for i in range(n-k):
    arr.append(arr[i]-num[i]+num[k+i])

print(max(arr))
'''
    
#누적 합 3단계 11659번
'''
import sys
input=sys.stdin.readline

S = list(input().rstrip())
count = [[0] * 26 for _ in range(len(S) + 1)]
for i in range(1, len(S) + 1):
    count[i] = count[i - 1].copy()
    count[i][ord(S[i - 1]) - 97] += 1

for _ in range(int(input())):
    temp = input().split()
    a, l, r = temp[0], int(temp[1]) + 1, int(temp[2]) + 1
    print(count[r][ord(a) - 97] - count[l - 1][ord(a) - 97])
'''
     
#누적 합 4단계 10986번
'''
import sys
input=sys.stdin.readline

n, m=map(int, input().split())
num=list(map(int, input().split()))

r=[0]*m
r[0]=1
arr=[0]
for i in range(1, n+1):
    arr.append((arr[i-1]+num[i-1])%m)
    r[arr[i]]+=1
    
ans=0
for i in range(0, m):
    ans+=r[i]*(r[i]-1)//2
print(ans)
'''

#누적 합 5단계 11660번
import sys
input=sys.stdin.readline

n, m=map(int, input().split())
arr = ([[0]*(n+1)]) + [[0] + list(map(int, input().split())) for _ in range(n)]

dp=[[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j]=dp[i][j-1]+dp[i-1][j]-dp[i-1][j-1]+arr[i][j]

for i in range(m):
    x1, y1, x2, y2=map(int, input().split())
    res=dp[x2][y2]-dp[x1-1][y2]-dp[x2][y1-1]+dp[x1-1][y1-1]
    print(res)
