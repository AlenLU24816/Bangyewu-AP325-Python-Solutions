def f(A,B):
    return [[(A[0][0]*B[0][0]+A[0][1]*B[1][0])%p,
             (A[0][0]*B[0][1]+A[0][1]*B[1][1])%p],

             [(A[1][0]*B[0][0]+A[1][1]*B[1][0])%p,
             (A[1][0]*B[0][1]+A[1][1]*B[1][1])%p]]

Dict = {
    0:0,
    1:1,
    2:1
}
p = 1000000007
while 1:

    n = int(input())
    if n == -1:
        break
    A = [[0,1],
        [1,1]]
    F = [[1,0],
        [0,1]]
    if n<3:
        print(Dict[n])
    else:
        n-=2
        while n > 1:
            if n&1:
                F =f(A,F)
                n-=1
            n>>=1
            A = f(A,A)
        F =f(A,F)

        print((F[0][1]+F[1][1])%p)