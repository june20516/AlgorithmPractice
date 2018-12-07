#10250

t = int(input())

for i in range(t):
	nums = list(map(int, input().split()))
	h = nums[0]
	w = nums[1]
	n = nums[2]
	
	xx = int(n/h) if n%h == 0 else int(n/h)+1
	yy = h if n%h == 0 else n%h
	
	print('{y}{x:0>2}'.format(y = yy, x = xx))




#2775
t = int(input())

for i in range(t):
    k = int(input())
    n = int(input())

    floor = []

    for i in range(n):
        floor.append(i+1)

    for i in range(k):
        for j in range(n-1):
            floor[j+1]  += floor[j]
        
    print(floor[n-1])