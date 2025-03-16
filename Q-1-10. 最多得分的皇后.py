n = int(input())
data = [list(map(int,input().split())) for _ in range(n)]
def nqueen(Queens, ijplus, ijminus, i, Sum):
    global Max
    if sum(pruning[i:])+Sum <= Max:
        return
    if i == n:
        Max = max(Max,Sum)
        return
    for j in range(n):
        if j not in Queens and j+i not in ijplus and i-j not in ijminus:
            Queens.add(j)
            ijplus.add(i+j)
            ijminus.add(i-j)
            nqueen(Queens, ijplus, (ijminus), i+1, Sum+data[i][j])
            Queens.remove(j)
            ijplus.remove(i+j)
            ijminus.remove(i-j)
    nqueen(Queens, ijplus, ijminus, i+1, Sum)
        
pruning = [max(row) for row in data]
Max = -101
nqueen(set(), set(), set(), 0, 0)
print(Max)