S = input()
area = int(input()) ** 2

ans = 0
stack = []
last_stack = 0


for s in S:
    if s != "2": #s = 0,1
        if s == "1":
            ans += area
        last_stack+=1
        while last_stack == 4:
            last_stack = stack.pop()+1
            area<<=2

    else: # s = 2
        area>>=2
        stack.append(last_stack)
        last_stack = 0
        

print(ans)