n = int(input())
Dict = dict()
for i in list(map(int,input().split())):
    if i not in Dict:
        Dict[i] = 0
    Dict[i]+=1
print(len(Dict))
print(*sorted(list(Dict.keys())))
