n = int(input())
graph = dict()
total_length = 0
for _ in range(n-1):
    a, b, length = map(int,input().split())
    total_length += length #need*2
    if a not in graph:
        graph[a] = []
    if b not in graph:
        graph[b] = []
    graph[a].append(b)
    graph[b].append(a)

for i in range(n):
    graph[i].sort()

# print(graph)

back_stack = []
output = [0]
Seen = {0}
back = False
for _ in range((n-1)*2):
    # print()
    point = output[-1]
    # print("point:",point)
    back = True
    for next_point in graph[point]:
        if next_point not in Seen:
            Seen.add(next_point)
            output.append(next_point)
            # print("output",output)
            back_stack.append(point)
            # print("back_stack",back_stack)
            back = False
            break
    if back:
        output.append(back_stack.pop())
    #     print("output",output)
    # print()

print(total_length*2)
print(*output)