#분할 정복 1단계 2630번
'''
import sys
input=sys.stdin.readline

n=int(input())
paper=[[0]*n for _ in range(n)]

for i in range(n):
    paper[i]=list(map(int, input().split()))

white=0
blue=0

def make_colorpaper(num, paper):
    global white
    global blue
    a=0

    for i in range(num):
        a+=sum(paper[i])

    if a==0:
        white+=1
    elif a==num*num:
        blue+=1
    else:
        temp=[paper[i][0:num//2] for i in range(num//2)]
        make_colorpaper(num//2, temp)
        temp=[paper[i][num//2:num] for i in range(num//2)]
        make_colorpaper(num//2, temp)
        temp=[paper[i][0:num//2] for i in range(num//2, num)]
        make_colorpaper(num//2, temp)
        temp=[paper[i][num//2:num] for i in range(num//2, num)]
        make_colorpaper(num//2, temp)
        
make_colorpaper(n, paper)
print(white)
print(blue)
'''

#분할 정복 2단계 1992번
'''
import sys
input=sys.stdin.readline

n=int(input())
video=[[0]*n for _ in range(n)]

for i in range(n):
    video[i]=list(map(int, list(input().strip())))

def qaud_tree(num, information):
    total=0

    for i in range(num):
        total+=sum(information[i])

    if total==0:
        print(0, end='')
    elif total==num*num:
        print(1, end='')
    else:
        print('(',end='')
        temp=[information[i][0:num//2] for i in range(num//2)]
        qaud_tree(num//2, temp)
        temp=[information[i][num//2:num] for i in range(num//2)]
        qaud_tree(num//2, temp)
        temp=[information[i][0:num//2] for i in range(num//2, num)]
        qaud_tree(num//2, temp)
        temp=[information[i][num//2:num] for i in range(num//2, num)]
        qaud_tree(num//2, temp)
        print(')',end='')
        
qaud_tree(n, video)
'''

#분할 정복 3단계 1780번
'''
import sys
input=sys.stdin.readline

n=int(input())
paper=[[0]*n for _ in range(n)]

for i in range(n):
    paper[i]=list(map(int, input().split()))

result=[0, 0, 0]

def cut_paper(x, y, num):
    global paper
    global result

    if num==1:
        result[paper[x][y]+1]+=1
    else:
        first = paper[x][y]
        sa=True
        for i in range(num):
            for j in range(num):
                if(paper[x+i][y+j]!=first):
                    sa=False
                    break
            if sa==False:
                break   
        if sa:
            result[paper[x][y]+1]+=1
        else:
            a=num//3
            for i in range(3):
                for j in range(3):
                    cut_paper(x+a*i, y+a*j, a)

cut_paper(0, 0, n)
print(result[0])
print(result[1])
print(result[2])
'''

#분할 정복 4단계 1629번
'''
import sys
input=sys.stdin.readline

a, b, c=map(int, input().split())

def invol(a, b):
    if b==1:
        return a%c
    else:
        temp=invol(a, b//2)
        if b%2==0:
            return temp*temp%c
        else:
            return temp*temp*a%c

print(invol(a, b))
'''

#분할 정복 5단계 11401번
'''
import sys
input=sys.stdin.readline

n, k=map(int, input().split())
p=1000000007

dp=[1]*(n+1)
for i in range(2, n+1):
    dp[i]=i*dp[i-1]%p

def pow(a, b):
    if b==1:
        return a%p
    elif b%2==0:
        return pow(a, b//2)**2 % p
    elif b%2==1:
        return a * (pow(a, b//2)**2) % p

a=dp[n]
b=dp[n-k] * dp[k] % p

print(a * pow(b, p - 2) % p)
'''

#분할 정복 6단계 2740번
'''
import sys
input=sys.stdin.readline

n, m=map(int, input().split())
a=[list(map(int, input().split())) for _ in range(n)]
m, k=map(int, input().split())
b=[list(map(int, input().split())) for _ in range(m)]

result=[[0]*k for _ in range(n)]

for i in range(n):
    for j in range(k):
        for h in range(m):
            result[i][j]+=a[i][h]*b[h][j]

for i in range(n):
    for j in range(k):
        print(result[i][j])
'''

#분할 정복 7단계 10830번
'''
import sys
input=sys.stdin.readline

n, b=map(int, input().split())
a=[list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        a[i][j]%=1000

def mul(a, b):
    global n
    res=[[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                res[i][j]+=a[i][k]*b[k][j]
            res[i][j]%=1000
    return res

def div(a, b):
    if b==1:
        return a
    elif b%2==0:
        temp=div(a, b//2)
        return mul(temp, temp)
    elif b%2==1:
        temp=div(a, b//2)
        return mul(mul(temp, temp), a)
    
ans = div(a, b)
for a in ans:
    print(*a)
'''
        
#분할 정복 8단계 11444번
'''
import sys
input=sys.stdin.readline

n=int(input())

def mul(a, b):
    p=1000000007
    res=[[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                res[i][j]+=a[i][k]*b[k][j]
            res[i][j]%=p
    return res

def fibonacci(n):
    a=[[1, 1], [1, 0]]
    if n==1:
        return a
    elif n%2==1:
        temp=fibonacci(n//2)
        return mul(mul(temp, temp), a)
    elif n%2==0:
        temp=fibonacci(n//2)
        return mul(temp, temp)
    
print(fibonacci(n)[1][0])
'''

#분할 정복 9단계 6549번 #다시 풀기

import sys
input=sys.stdin.readline

while True:
    num=list(map(int, input().split()))+[0]

    n=num[0]
    if n==0:
        break
    
    arr=[(1, num[1])]
    ans=0
    for i in range(2, n+2):
        cur=i
        while arr and arr[-1][1]>num[i]:
          cur,h=arr.pop()
          ans=max(ans,(i-cur)*h)
        arr.append((cur, num[i]))
    print(ans)
