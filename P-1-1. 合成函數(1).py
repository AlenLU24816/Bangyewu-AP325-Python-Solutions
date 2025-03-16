def f():
    global index
    index+=1
    if data[index] == "f":
        num1 = f()
        return 2*num1-1
    elif data[index] == "g":
        num1 = f()
        num2 = f()
        return num1+2*num2-3
    else:
        return int(data[index])

index = -1
data = list(input().split())
print(f())