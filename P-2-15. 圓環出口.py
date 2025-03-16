import bisect
n, m = map(int,input().split())
circle = list(map(int,input().split()))
keys = list(map(int,input().split()))
for i in range(1,len(circle)):
    circle[i]+= (circle[i-1])
# print(circle)
# print(keys)

last_key = 0
for key in keys:
    index = bisect.bisect(circle,(key+last_key-0.5)%circle[-1])
    last_key = circle[index]
    # print(index)
print((index+1)%len(circle))