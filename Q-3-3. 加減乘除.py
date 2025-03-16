S = input()
nums = [int(S[0])]
operator = []
for i in range(1,len(S)-1,2):
    if S[i] == "*":
        num = int(nums.pop())
        nums.append(num*int(S[i+1]))

    elif S[i] == "/":
        num = int(nums.pop())
        nums.append(num//int(S[i+1]))

    else:
        operator.append(S[i])
        nums.append(int(S[i+1]))


ans = nums[0]
for i in range(len(operator)):
    if operator[i] == "+":
        ans+=nums[i+1]
    else:
        ans-=nums[i+1]
print(int(ans))
