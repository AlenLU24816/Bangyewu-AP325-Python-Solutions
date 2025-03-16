def main():
    n = int(input())
    data = [float("inf")] + list(map(int,input().split()))
    stack = [0]
    ans = 0
    for i in range(1,n+1):
        while(data[stack[-1]] <= data[i]):
            stack.pop()
        ans += (i - stack[-1])
        stack.append(i)
    print(ans)
main()