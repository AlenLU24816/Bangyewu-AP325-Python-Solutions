def main():
    n, k = map(int,input().split())
    data = sorted(list(set(map(int,input().split()))))
    n = len(data)

    def put(Range):
        i = 0
        for _ in range(k):
            Max_value = data[i]+Range
            while i+1 < n and data[i+1] <= Max_value:
                i+=1
            if i+1 < n:
                i+=1
            else:
                return True
        return False
            
    l = 1
    r = (data[-1]-data[0]-k+1)//k
    jump = (r-l)//2
    while jump:
        while not put(l+jump) and l+jump<=r:
            l+=jump
        jump//=2
    print(l+1)

main()