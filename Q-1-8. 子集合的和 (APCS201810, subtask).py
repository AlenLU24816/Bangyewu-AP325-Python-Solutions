def main():
    import bisect
    n, target = map(int,input().split())
    data = list(map(int,input().split()))

    pre_set = set()
    for i in data[:n//2]:
        Len = len(pre_set)
        for j in list(pre_set):
            value = i+j
            if value <= target and value not in pre_set:
                pre_set.add(value)
        if i <= target and i not in pre_set:
            pre_set.add(i)
    # print(pre_set)
    pre_list = sorted(list(pre_set))

    post_set = set()
    for i in data[n//2:]:
        Len = len(post_set)
        for j in list(post_set):
            value = i+j
            if value <= target and value not in post_set:
                post_set.add(value)
        if i <= target and i not in post_set:
            post_set.add(i)

    # print(pre_list)
    # print(post_set)
    def f():
        Max = -1
        for i in post_set:
            # l = 0
            # r = len(pre_list)-1
            # jump = (l+r)//2
            # while jump:
            #     while l+jump < len(pre_list) and i+pre_list[l+jump] <= target:
            #         l+=jump
            #     jump//=2
            value = pre_list[bisect.bisect(pre_list,target-i)-1] + i
            if value < target:
                Max = max(Max, value)
            if value == target:
                Max = target
                return Max
        return Max
    print(f())
main()
"""
5 17
5 5 8 3 10

6 15
2 3 4 2 1 6
"""