#그리디 알고리즘 1단계 11047번
'''
import sys
input=sys.stdin.readline

n, k=map(int, input().split())
coin=sorted([int(input()) for _ in range(n)], reverse=True)
ans=0

for i in range(n):
    ans+=k//coin[i] #가장 큰 값부터 계산
    k%=coin[i]

print(ans)
'''

#그리디 알고리즘 2단계 1931번
'''
import sys
input=sys.stdin.readline

n=int(input())

time=[]
for _ in range(n):
    start, end=map(int, input().split())
    time.append([start, end])

time.sort(key=lambda x:x[0])
time.sort(key=lambda x:x[1])

print(time)
ans=0
j=0

for i in range(len(time)):
    k=time[i][0]
    if k>=j:
        ans+=1
        j=time[i][1]
        
print(ans)
'''

#그리디 알고리즘 3단계 11399번
'''
import sys
input=sys.stdin.readline

n=int(input())
time=list(map(int, input().split()))

time=sorted(time, reverse=False)

dp=[0]
for i in range(n):
    dp.append(time[i]+dp[i])

print(sum(dp))
'''

#그리디 알고리즘 4단계 1541번
'''
import sys
input=sys.stdin.readline

num=input()

dp=[]
for i in num.split('-'):
    sum=0
    for j in i.split('+'):
        sum+=int(j)
    dp.append(sum)
    
ans=dp[0]
for i in range(1, len(dp)):
    ans-=dp[i]
print(ans)
'''

#그리디 알고리즘 5단계 13305번

import sys
input=sys.stdin.readline

n=input()
road=list(map(int, input().split()))
oil=list(map(int, input().split()))

money=oil[0]*road[0]
l=oil[0]

for i in range(1, len(road)):
    if oil[i]<=l:
        l=oil[i]
    money+=l*road[i]
    
print(money)



