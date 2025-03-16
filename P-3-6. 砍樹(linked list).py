n, J = map(int,input().split())
tree_index = [0] + list(map(int,input().split())) + [J]
tree_hight = [J+1] + list(map(int,input().split())) + [J+1]
link_pre = [0] + [i for i in range(n+1)]
link_next = [i for i in range(1,n+2)] + [n+1]
stack = []
alive = [False] + [True]*n + [False]
for i in range(1,n+1):
    if tree_index[i] - tree_hight[i] >= tree_index[i-1] or tree_index[i] + tree_hight[i] <= tree_index[i+1]:
        stack.append(i)
        alive[i] = False
hightest = 0
down_tree = 0
while(stack):
    index = stack.pop()
    hightest = max(hightest,tree_hight[index])
    if alive[link_pre[index]] and tree_index[link_pre[index]] + tree_hight[link_pre[index]] <= tree_index[link_next[index]]:
        stack.append(link_pre[index])
        alive[link_pre[index]] = False
    if alive[link_next[index]] and tree_index[link_next[index]] - tree_hight[link_next[index]] >= tree_index[link_pre[index]]:
        stack.append(link_next[index])
        alive[link_next[index]] = False
    link_next[link_pre[index]] = link_next[index]
    link_pre[link_next[index]] = link_pre[index]
    down_tree+=1
print(down_tree)
print(hightest)