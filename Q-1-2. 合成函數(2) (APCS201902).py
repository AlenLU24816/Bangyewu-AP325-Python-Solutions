def f():
    global index
    index+=1
    if data[index] == "f":
        x = f()
        return 2*x-3
    elif data[index] == "g":
        x = f()
        y = f()
        return 2*x+y-7
    elif data[index] == "h":
        x = f()
        y = f()
        z = f()
        return 3*x-2*y+z
    else:
        return int(data[index])

index = -1

data = list(input().split())
print(f())