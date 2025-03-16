def main():
    n = int(input())
    Dict = {1:0}
    for i in list(map(int,input().split())):
        i%=10009
        for j, count in list(Dict.items()):
            value = (i*j)%10009
            Dict[value] = Dict.get(value, 0) + count
        Dict[i] = Dict.get(i,0) + 1
        
    print(Dict[1])
main()