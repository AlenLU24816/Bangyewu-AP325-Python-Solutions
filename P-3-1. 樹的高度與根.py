import sys
sys.setrecursionlimit(9999999)
def DFS(point):
    global ans
    deep = [0]
    for i, p in enumerate(graph[point]):
        deep[i]+=(DFS(p))
        deep.append(0)

    # print(max(deep)+1)
    ans += max(deep)
    return max(deep)+1


n = int(input())
Seen = {i+1 for i in range(n)}
graph = dict()
for i in range(1,n+1):
    data = list(map(int,input().split()))
    graph[i] = []
    if data[0]:
        for j in data[1:]:
            Seen.remove(j)
            graph[i].append(j)

Seen = list(Seen)
print(Seen[0])
ans = 0
DFS(Seen[0])
print(ans)