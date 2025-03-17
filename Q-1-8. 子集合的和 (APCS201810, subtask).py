# from itertools import islice
n, limit = map(int,input().split())
Set = set()
Max = -1
for input_num in map(int,input().split()):
    if input_num <= limit:
        i = 0
        list_set = list(Set)
        for set_num in list_set:
            Sum = input_num+set_num
            if Sum <= limit and Sum not in Set:
                Set.add(Sum)
                Max = max(Max,Sum)
        if input_num not in Set:
            Set.add(input_num)
print(Max)