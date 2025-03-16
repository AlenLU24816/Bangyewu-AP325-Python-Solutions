n, deep_limit = map(int,input().split())
stick = list(map(int,input().split()))
lsum = [0]*n
rsum = [0]*n
for i in range(len(stick)-1):
    lsum[i+1] = lsum[i] + stick[i]
    rsum[-2-i] = rsum[-i-1] + stick[-i-1]

def cut(left, right, deep):
    if right - left < 2 or deep == deep_limit:
        return 0
    elif right - left == 2:
        return stick[left+1]
    cut_point = 0
    last_diff = (sum(rsum[left+1:right+1]) - (rsum[right]*(right-left))) - (lsum[left+1] - lsum[left])
    for i in range(left+2,right):
        cut_point = i
        diff = last_diff - (lsum[i] - lsum[left]) - (rsum[i-1] - rsum[right])
        if diff <= 0:
            break
        last_diff = diff
    if last_diff <= diff*-1:
        cut_point-=1
        pass

    return cut(left, cut_point-1, deep+1) + cut(cut_point+1, right, deep+1) + stick[cut_point]
    




print(cut(0, n-1, 0))