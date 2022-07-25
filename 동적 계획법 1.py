#동적 계획법 1 1단계 24416번
'''
def fn2(n):
    global l, c
    if n == 0: return l[0]
    elif n == 1: return l[1]
    else:
        for i in range(2, n+1):
            c += 1
            num = l[i-1] + l[i-2]
            l.append(num)
        return l[n]
        
l = [0, 1]
c = 0

n = int(input())
print(fn2(n), c-1)
'''

#동적 계획법 1 2단계 9184번
'''
import sys
input = sys.stdin.readline

def w(a, b, c):
    if dp[a+50][b+50][c+50] != 0:
        return dp[a+50][b+50][c+50]
    
    if a <= 0 or b <= 0 or c <= 0:
        dp[a+50][b+50][c+50] = 1
        return dp[a+50][b+50][c+50]
    if a > 20 or b > 20 or c > 20:
        dp[a+50][b+50][c+50] = w(20, 20, 20)
        return dp[a+50][b+50][c+50]
    if a < b and b < c:
        dp[a+50][b+50][c+50] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return dp[a+50][b+50][c+50]
    else:
        dp[a+50][b+50][c+50] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return dp[a+50][b+50][c+50]


dp = [[[0 for _ in range(101)] for _ in range(101)] for _ in range(101)]
while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    print(f'w({a}, {b}, {c}) = {w(a,b,c)}')
'''

#동적 계획법 1 3단계 1904번
'''
#an=a(n-1)+a(n-2)
import sys
input=sys.stdin.readline

n=int(input().strip())

dp1=1 #N=1일 때의 값
dp2=2 #N=2일 때의 값

if n<=2:
    print(n)
else:
    for i in range(3, n+1):
        an=dp1+dp2
        dp1=dp2%15746
        dp2=an%15746
    print(an%15746)
'''

#동적 계획법 1 4단계 9461번
'''첫번째 방법
#p(n)=p(n-1)+p(n-5)  5<n<=100
import sys
input=sys.stdin.readline

t=int(input().strip())

p=[1, 1, 1, 2, 2]

for _ in range(t):
    n=int(input().strip())
    if n<=5:
        print(p[n-1])
    else:
        p=[1, 1, 1, 2, 2]
        for i in range(6, n+1):
            dp=p[i-2]+p[i-6]
            p.append(dp)
        print(p[n-1])
'''
'''두번째 방법
import sys
input=sys.stdin.readline

t=int(input().strip())

for _ in range(t):
    n=int(input().strip())
    if n<=5:
        p=[1, 1, 1, 2, 2]
        print(p[n-1])
    else:
        p=[1, 1, 1, 2, 2]
        for _ in range(n-5):
            dp=p[4]+p[0]
            for i in range(4):
                p[i]=p[i+1]
            p[4]=dp
        print(dp)
'''

#동적 계획법 1 5단계 1912번
'''
import sys
input=sys.stdin.readline

n=int(input().strip())
arr=list(map(int, input().split()))

for i in range(1, n):
    arr[i]=max(arr[i], arr[i-1]+arr[i])

print(max(arr))
'''

#동적 계획법 1 6단계 1149번
'''
import sys
input=sys.stdin.readline

n=int(input().strip())
rgb=[]
for _ in range(n):
    r, g, b=map(int, input().split())
    rgb.append([r, g, b])

for i in range(1, n):
    rgb[i][0]=rgb[i][0]+min(rgb[i-1][1], rgb[i-1][2])
    rgb[i][1]=rgb[i][1]+min(rgb[i-1][0], rgb[i-1][2])
    rgb[i][2]=rgb[i][2]+min(rgb[i-1][0], rgb[i-1][1])

res=min(rgb[n-1][0], rgb[n-1][1], rgb[n-1][2])
print(res)
'''

#동적 계획법 1 7단계 1932번
'''
import sys
input=sys.stdin.readline

dp=[]
n=int(input().strip())
for i in range(n):
    dp.append(list(map(int, input().split())))

    
for i in range(1, n):
    dp[i][0]=dp[i][0]+dp[i-1][0]
    for j in range(1, i):
        dp[i][j]=dp[i][j]+max(dp[i-1][j-1], dp[i-1][j])
    dp[i][i]=dp[i][i]+dp[i-1][i-1]

print(max(dp[n-1]))
'''

#동적 계획법 1 8단계 2579번
'''#1 왜 런타임에러(indexerror)가 뜨는지
import sys
input=sys.stdin.readline

stair=[]
n=int(input().strip())
for i in range(n):
    stair.append(int(input().strip()))

dp=[0 for _ in range(n)]
dp[0]=stair[0]
dp[1]=max(stair[0]+stair[1], stair[1])
dp[2]=max(stair[0]+stair[2], stair[1]+stair[2])

for i in range(3, n):
    dp[i]=max(stair[i]+dp[i-2], stair[i]+stair[i-1]+dp[i-3])

print(dp[n-1])
'''
'''#2
import sys
input=sys.stdin.readline

stair=[0 for _ in range(301)]
n=int(input().strip())
for i in range(n):
    stair[i]=int(input().strip())

dp=[0 for _ in range(301)]
dp[0]=stair[0]
dp[1]=max(stair[0]+stair[1], stair[1])
dp[2]=max(stair[0]+stair[2], stair[1]+stair[2])

for i in range(3, n):
    dp[i]=max(stair[i]+dp[i-2], stair[i]+stair[i-1]+dp[i-3])
print(dp[n-1])
'''

#동적 계획법 1 9단계 1463번

'''#1
import sys
input=sys.stdin.readline

n=int(input().strip())
dp=[0 for _ in range(n+1)]

for i in range(2, n+1):
    if i%2==0 and i%6!=0:
        dp[i]=1+min(dp[int(i//2)], dp[i-1])
    elif i%3==0 and i%6!=0:
        dp[i]=1+min(dp[int(i//3)], dp[i-1])
    elif i>5 and i%6==0:
        dp[i]=1+min(min(dp[int(i//3)], dp[i-1]), min(dp[int(i//2)], dp[i-1]))
    else:
        dp[i]=1+dp[i-1]
        
print(dp[n])
'''

#동적 계획법 1 10단계 10844번
'''
import sys
input=sys.stdin.readline

n=int(input().strip())
dp=[[0 for _ in range(10)] for _ in range(n)]

dp[0][0]=0
for i in range(1, 10):
    dp[0][i]=1

for i in range(1, n):
    dp[i][0]=dp[i-1][1]%1000000000
    for j in range(1, 9):
        dp[i][j]=(dp[i-1][j-1]+dp[i-1][j+1])%1000000000
    dp[i][9]=dp[i-1][8]%1000000000

res=sum(dp[n-1])%1000000000
print(res)
'''

#동적 계획법 1 11단계 2156번
'''
import sys
input=sys.stdin.readline

n=int(input().strip())
g=[0 for _ in range(n)]
dp=[[0 for _ in range(3)] for _ in range(n)]

for i in range(n):
    g[i]=int(input().strip())

dp[0]=[0, g[0], g[0]]

for i in range(1, n):
    dp[i][0]=max(dp[i-1])
    dp[i][1]=dp[i-1][0]+g[i]
    dp[i][2]=dp[i-1][1]+g[i]
print(max(dp[n-1]))
'''

#동적 계획법 1 12단계 11053번
'''
import sys
input=sys.stdin.readline

n=int(input().strip())
arr=list(map(int, input().split()))
dp=[0 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if arr[i]>arr[j] and dp[i]<dp[j]:
            dp[i]=dp[j]
    dp[i]+=1

print(max(dp))
'''

#동적 계획법 1 13단계 11054번
'''
import sys
input=sys.stdin.readline

n=int(input().strip())
arr=list(map(int, input().split()))
left=[1 for _ in range(n)]
right=[1 for _ in range(n)]
dp=[]

for i in range(n):
    for j in range(i):
        if arr[i]>arr[j]:
            left[i]=max(left[j]+1, left[i])
        if arr[n-1-i]>arr[n-1-j]:
            right[n-1-i]=max(right[n-1-j]+1, right[n-1-i])
for i in range(n):
    dp.append(left[i]+right[i]-1)
print(max(dp))
'''

#동적 계획법 1 14단계 2565번
'''
import sys
input=sys.stdin.readline

n=int(input().strip())
arr=[0 for _ in range(501)]
dp=[1 for _ in range(501)]

for _ in range(n):
    a, b=map(int, input().split())
    arr[a]=b

for i in range(1, 501):
    for j in range(i):
        if arr[i]>arr[j] and arr[i]!=0 and arr[j]!=0:
            dp[i]=max(dp[j]+1, dp[i])
res=n-max(dp)
print(res)
'''

#동적 계획법 1 15단계 9251번
'''
import sys
input=sys.stdin.readline

first=input().strip()
second=input().strip()

dp = [[0 for _ in range(len(second) + 1)] for _ in range(len(first) + 1)]
for i in range(1, len(first)+1):
    for j in range(1, len(second)+1):
        if first[i-1]==second[j-1]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j], dp[i][j-1])

res=dp[len(first)][len(second)]
print(res)
'''
#동적 계획법 1 16단계 12865번

import sys
input = sys.stdin.readline

n, k=map(int, input().split())
dp=[0 for _ in range(k+1)]

for _ in range(n):
    w, v = map(int, input().split())
    for j in range(k, w-1, -1):
        dp[j] = max(dp[j], dp[j-w] + v)
        
print(dp[-1])
