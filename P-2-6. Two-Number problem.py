a,b,k = map(int,input().split())
target = set()
for i in tuple(map(int,input().split())):
    target.add(k-i)
ans = 0
for i in tuple(map(int,input().split())):
    if i in target:
        ans+=1
print(ans)