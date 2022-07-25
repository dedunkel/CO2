#정렬 1단계 2750번
'''
n=int(input())
num=[]

for i in range(n):
    k=int(input())
    num.append(k)
    
for i in range(n-1):
    for j in range(i+1, n, 1):
        if num[i]>num[j]:
            temp=num[i]
            num[i]=num[j]
            num[j]=temp

for i in range(n):
    print(num[i])
'''
#정렬 2단계 2751번
'''
import sys

n=int(input())
num=[]

for i in range(n):
    num.append(int(sys.stdin.readline()))
    
num=sorted(num, reverse=False)

for i in range(n):
    print(num[i])
'''

#정렬 3단계 10989번
'''
import sys

n=int(input())

count=[0 for i in range(100000)]

for i in range(n):
    count[int(sys.stdin.readline())-1] += 1
    
for i in range(100000):
    if count[i] != 0:
        for j in range(count[i]):
            print(i+1)
'''

#정렬 4단계 2108번
'''
from collections import Counter
import sys

n=int(input())
num=[]

for i in range(n):
    num.append(int(sys.stdin.readline()))

num.sort()

#산술평균
total=0
for i in range(n):
    total+=num[i]
print(round(total/n))

#중앙값
print(num[n//2])

#최빈값
counts=Counter(num).most_common()
if n>1:
    if counts[0][1]==counts[1][1]:
        print(counts[1][0])
    else:
        print(counts[0][0])
else:
    print(counts[0][0])

#범위
print(max(num)-min(num))
'''

#정렬 5단계 1427번
'''
n=input()
len=(len(str(n)))
n=int(n)
num=[]

for _ in range(len):
    num.append(n%10)
    n=n//10

num.sort(reverse=True)

i=1
a=0
for j in range(len-1, -1, -1):
    a+=num[j]*i
    i*=10
print(a)
'''

#정렬 6단계 11650번
'''
n=int(input())
arr=[]

for _ in range(n):
    x, y = map(int, input().split())
    arr.append([x, y])

arr.sort()

for i in range(n):
    print(arr[i][0], arr[i][1])
'''

#정렬 7단계 11650번
'''
n=int(input())
arr=[]

for _ in range(n):
    x, y = map(int, input().split())
    arr.append([x, y])

arr.sort(key=lambda x:(x[1], x[0]))

for i in range(n):
    print(arr[i][0], arr[i][1])
'''

#정렬 8단계 1181번
'''
n=int(input())
arr=[[0 for col in range(2)] for row in range(n)]

for i in range(n):
    string=str(input())
    arr[i][0] = string
    arr[i][1] = len(string)

res=[]
for i in arr:
    if i not in res:
        res.append(i)
        
res.sort(key = lambda x : (x[1], x[0]))
for i in range(len(res)):
    print(res[i][0])
'''
#정렬 9단계 10814번
'''    
n=int(input())
arr=[]

for i in range(n):
    age, name = map(str,input().split())
    arr.append([int(age), name, i])

arr.sort(key = lambda x : (x[0], x[2]))

for i in range(n):
    print(arr[i][0], arr[i][1])
'''
#정렬 10단계 18870번
n=int(input())
nums=list(map(int, input().split()))
num=sorted(set(nums))

dic={}

for i in range(len(num)):
    dic[num[i]]=i

for i in nums:
    print(dic[i], end=' ')
    


