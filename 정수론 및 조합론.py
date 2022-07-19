#정수론 및 조합론 1단계 5086번
'''
import sys
input = sys.stdin.readline

while True:
    arr=input().split()
    a=int(arr[0])
    b=int(arr[1])

    if a<b:
        if b%a==0:
            print("factor")
        else:
            print("neither")
    elif a>b:
        if a%b==0:
            print("multiple")
        else:
            print("neither")
    elif a==0 and b==0:
        break
    else:
        print("neither")
'''

#정수론 및 조합론 2단계 1037번
'''
import sys
input=sys.stdin.readline

n=int(input().strip())
num=list(map(int, input().split()))
if n==1:
    print(num[0]*num[0])
else:
    print(max(num)*min(num))
'''

#정수론 및 조합론 3단계 2609번
'''
import sys
input=sys.stdin.readline

a, b = map(int, input().split())
cd=[]

for i in range(1, max(a,b)+1):
    if a%i==0 and b%i==0:
        cd.append(int(i))

gcd=max(cd)
lcm=gcd*(a//gcd)*(b//gcd)

print(gcd)
print(lcm)
'''
#정수론 및 조합론 4단계 1934번
'''
import sys
input=sys.stdin.readline

def lcm(a, b):
    cp_a=a
    cp_b=b
    while b!=0:
        tmp = a
        a=b
        b=tmp%b
        
    return cp_a*cp_b//a
    
t=int(input().strip())

res=[]
for i in range(t):
    a, b= map(int, input().split())
    res.append(int(lcm(a, b)))
    
for i in res:
    print(i)
'''    

#정수론 및 조합론 5단계 2981번
'''
import sys
input=sys.stdin.readline

def gcd(a, b):
    while b!=0:
        tmp = a
        a=b
        b=tmp%b
        
    return a

n=int(input().strip())
num=[]
a=[]
for i in range(n):
    num.append(int(input().strip()))
num.sort()

ans=num[1]-num[0]
for i in range(2, n):
    ans=gcd(ans, num[i]-num[i-1])

for i in range(2, int(ans**0.5)+1): #시간 초과의 원인/수정 전 코드: for i in range(2, ans+1):
    if ans%i==0:
        a.append(i)
        a.append(ans//i)
a.append(ans)
a=list(set(a))
a.sort()
for i in a:
    if i!=1:
        print(i, end=' ')
'''

#정수론 및 조합론 6단계 3036번
'''
import sys
input=sys.stdin.readline

def gcd(a, b):
    while b!=0:
        tmp = a
        a=b
        b=tmp%b
        
    return a

n=int(input().strip())
rings=list(map(int, input().split()))

for i in range(1, n):
    g=gcd(rings[0], rings[i])
    print(str(rings[0]//g)+'/'+str(rings[i]//g))
'''

#정수론 및 조합론 7단계 11050번
'''
def factorial(n):
    if n<=1:
        fac[n]=1
    else:
        fac[n]=n*factorial(n-1)
    return fac[n]

n, k=map(int, input().split())
fac=[0 for _ in range(n+1)]
print(factorial(n)//(factorial(k)*factorial(n-k)))
'''

#정수론 및 조합론 8단계 11051번
#정수론 및 조합론 9단계 1010번
'''
import sys
input=sys.stdin.readline

def factorial(n):
    if n<=1:
        return 1
    else:
        return n*factorial(n-1)

t=int(input().strip())
for i in range(t):
    n, m=map(int, input().split())

    print(factorial(m)//(factorial(n)*factorial(m-n)))
'''

#정수론 및 조합론 10단계 9375번
'''
import sys
input=sys.stdin.readline

t=int(input().strip())
for _ in range(t):
    n=int(input().strip())
    dic={}
    res=1
    for _ in range(n):
        kind_list=list(dic.keys())
        name, kind = map(str, input().split())
        dic[kind]=dic.get(kind, 0)
        if kind not in kind_list or not dic[kind]:
            dic[kind]=1
        else:
            dic[kind]+=1
    total=list(dic.values())
    for i in total:
        res*=i+1
    res-=1
    print(res)
'''

#정수론 및 조합론 11단계 1676번
'''
import sys
input=sys.stdin.readline

def factorial(n):
    if n<=1:
        return 1
    else:
        return n*factorial(n-1)
    
n=int(input().strip())

fac=factorial(n)

count=0
i=10
str_fac=str(fac)
for _ in range(len(str_fac)):
    if fac%i==0:
        count+=1
    else:
        break
    i*=10
print(count)
'''

#정수론 및 조합론 12단계 2004번
def two(n):
    count=0
    while n!=0:
        n//=2
        count+=n
    return count

def five(n):
    count=0
    while n!=0:
        n//=5
        count+=n
    return count

n, m=map(int, input().split())
two_nm=two(n)-two(m)-two(n-m)
five_nm=five(n)-five(m)-five(n-m)

print(min(two_nm, five_nm))
