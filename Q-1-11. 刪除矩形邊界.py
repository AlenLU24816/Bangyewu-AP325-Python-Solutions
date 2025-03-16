I, J = map(int,input().split())
data = [list(input().split()) for _ in range(I)]

pi = [[(0,0)] for _ in range(I)]
for i in range(I):
    for j in range(1,J+1):
        if data[i][j-1] == "0":
            pi[i].append((1+pi[i][j-1][0],pi[i][j-1][1]))
        else:
            pi[i].append((pi[i][j-1][0],1+pi[i][j-1][1]))

pj = [[] for _ in range(I+1)]
pj[0] = [(0,0) for _ in range(J)]

for i in range(1,I+1):
    for j in range(J):
        if data[i-1][j] == "0":
            pj[i].append((pj[i-1][j][0]+1,pj[i-1][j][1]))
        else:
            pj[i].append((pj[i-1][j][0],pj[i-1][j][1]+1))

DP = dict()
def f(i1, i2, j1, j2):
    if (i1, i2, j1, j2) not in DP:
        # print()
        if i2-i1 == 1 or j2-j1 == 1:
            return 0
        
        U = f(i1+1, i2, j1, j2) + min(pi[i1][j2][0]-pi[i1][j1][0],pi[i1][j2][1]-pi[i1][j1][1])

        D = f(i1, i2-1, j1, j2) + min(pi[i2-1][j2][0]-pi[i2-1][j1][0],pi[i2-1][j2][1]-pi[i2-1][j1][1])

        L = f(i1, i2, j1+1, j2) + min(pj[i2][j1][0]-pj[i1][j1][0],pj[i2][j1][1]-pj[i1][j1][1])

        R = f(i1, i2, j1, j2-1) + min(pj[i2][j2-1][0]-pj[i1][j2-1][0],pj[i2][j2-1][1]-pj[i1][j2-1][1])
        # print(i1, i2, j1, j2,"|",U, D, L, R,min(U, D, L, R))
        # print()
        DP[(i1, i2, j1, j2)] = min(U, D, L, R)
    return DP[(i1, i2, j1, j2)]

print(f(0, I, 0, J))
"""
4 5
1 0 0 1 1
0 0 1 0 1
1 1 0 1 0
1 0 1 1 0

3 5
0 0 0 1 0
1 0 1 1 1
0 0 0 1 0

3 3
1 0 1
0 1 0
1 0 1
"""