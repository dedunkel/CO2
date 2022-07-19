#집합과 맵 1단계 10815번
'''
import sys
n=int(sys.stdin.readline())
nums1=list(map(int, sys.stdin.readline().split()))
m=int(sys.stdin.readline())
nums2=list(map(int, sys.stdin.readline().split()))
dic={num:1 for num in nums1}

for i in nums2:
    if dic.get(i, 0):
        print(1, end=' ')
    else:
        print(0, end=' ')
'''

#집합과 맵 2단계 14425번
'''
import sys
input=sys.stdin.readline
set1=[]
set2=[]
n, m=map(int, input().split())
for i in range(n):
    set1.append(input())

for i in range(m):
    set2.append(input())

count=0          
for i in set2:
    if i in set1:
        count+=1
print(count)
'''

#집합과 맵 3단계 1620번
'''
import sys
input=sys.stdin.readline

poketmon={}
n, m=map(int, input().split())

for i in range(n):
    a=input().strip()
    poketmon[a] = i+1
    poketmon[i+1] = a

for i in range(m):
    quest=input().strip()
    if quest.isdecimal()==True:
        print(poketmon[int(quest)])
    else:
        print(poketmon[quest])
'''

#집합과 맵 4단계 10816번
'''
import sys
input=sys.stdin.readline

n=int(input())
nums1=list(map(int, input().split(" ")))
m=int(input())
nums2=list(map(int, input().split(" ")))

dic={}

for i in nums1:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1

for i in nums2:
    if i in dic:
        print(dic[i], end=' ')
    else:
        print(0, end=' ')
'''

#집합과 맵 5단계 1764번
'''
import sys
input=sys.stdin.readline

n, m=map(int, input().split())
arr1=[]
arr2=[]
for i in range(n):
    arr1.append(input().strip())
for i in range(m):
    arr2.append(input().strip())

res=sorted(list(set(arr1)&set(arr2)))

print(len(res))
for i in res:
    print(i)
'''

#집합과 맵 6단계 1269번
'''
import sys
input=sys.stdin.readline

n, m=map(int, input().split())
set1=set(map(int, input().split(" ")))
set2=set(map(int, input().split(" ")))

print(len((set1-set2)|(set2-set1)))
'''

#집합과 맵 7단계 11478번
import sys
input=sys.stdin.readline

string=input().strip()
res=set()
for i in range(len(string)):
    for j in range(i, len(string)):
        res.add(string[i:j+1])
print(len(res))
