n, target = map(int,input().split())
Set = set()
for i in list(map(int,input().split())):
    if Set:
        inside_Set = set()
        for j in Set:
            if i+j not in Set and i+j <= target:
                inside_Set.add(j+i)
        Set.update(inside_Set)
        del inside_Set
    if i not in Set and i <= target:
        Set.add(i)
print(max(Set))