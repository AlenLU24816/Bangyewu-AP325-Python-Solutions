n = int(input())
data = sorted(list(map(int,input().split())))
for i in range(1,len(data)):
    data[i] += data[i-1]
print(sum(data))