n = int(input())
data = list(map(int,input().split()))
sorted_data = sorted(set(data))
Dict = dict()
for i in range(len(sorted_data)):
    Dict[sorted_data[i]] = i
for i in data:
    print(Dict[i],end=" ")