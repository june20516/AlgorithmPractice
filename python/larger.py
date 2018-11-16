#10817
raw = input().split()
nums = list(map(int,raw))
nums.sort()
print(nums[1])


#10871
N, X = input().split()
nums = list(map(int,input().split()))
ans = ""
for i in range(int(N)):
    if nums[i] < int(X):
        ans += str(nums[i]) + " "

print(ans)