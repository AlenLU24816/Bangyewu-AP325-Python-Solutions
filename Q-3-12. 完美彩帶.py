def main():
    Type, n = map(int,input().split())
    data = list(map(int,input().split()))
    Seen = set()
    left = 0
    ANS = 0
    for i in range(len(data)):
        if data[i] not in Seen:
            Seen.add(data[i])
        else:
            while(data[left] != data[i]):
                Seen.remove(data[left])
                left += 1
            left += 1
        if i-left+1 == Type:
            ANS+=1
    print(ANS)
main()