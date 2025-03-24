x,y,p = map(int,input().split())
ans = 1
x %= p
while y>0:
    if y&1:
        ans = (ans*x)%p
        y -= 1
    x = (x**2) % p
    y>>=1
print(ans)

"""
2 13 11
"""