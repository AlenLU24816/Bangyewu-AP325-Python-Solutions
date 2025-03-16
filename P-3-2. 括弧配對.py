while(1):
    stack = []
    Dict = {
        "(":")",
        "[":"]",
        "{":"}"
    }
    YN = True
    try:
        S = input()
    except:
        break
    for s in S:
        if s in Dict:
            stack.append(s)
        elif stack:
            sl = stack.pop()
            if Dict[sl] != s:
                YN = False
                break
        else:
            YN = False
            break
        
    if YN and not stack:
        print("yes")
    else:
        print("no")