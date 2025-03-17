def main():
    n = int(input())
    end = -1
    ans = 0
    for s,e in sorted((tuple(map(int,(input().split())))  for _ in range(n)), key = lambda x:x[1]):
        if end < s:
            end = e
            ans+=1
    print(ans)
main()