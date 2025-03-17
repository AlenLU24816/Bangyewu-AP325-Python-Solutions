t = int(input())
for _ in range(t):
    n = int(input())
    ans = 0
    if n >= 50:
        ans += n//50
        n%=50

    if n >= 10:
        ans += n//10
        n%=10

    if n >= 5:
        ans += n//5
        n%=5

    ans+=n
    print(ans)