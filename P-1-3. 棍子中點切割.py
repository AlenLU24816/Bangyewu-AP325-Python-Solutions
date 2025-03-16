def cut(left, right):
    if right-left <= 1:
        return 0
    target = (data[left]+data[right])//2
    cut_point = left
    jump = (right - left)//2
    while jump:
        while jump+cut_point < right and data[jump+cut_point] < target:
            cut_point+=jump
        jump//=2
    
    if target - data[cut_point] >= data[cut_point+1] - target:
        return data[right]-data[left] + cut(cut_point+1,right) + cut(left,cut_point+1)
    else:
        return data[right]-data[left] + cut(cut_point,right) + cut(left,cut_point)


n,l = map(int,input().split())
data = [0] + list(map(int,input().split())) + [l]
print(cut(0,n+1))