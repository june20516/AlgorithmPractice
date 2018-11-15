#1924
# a, b = input().split(" ")
# a = int(a)
# b = int(b)
def whatDay(a,b):
    dateOfMonth = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    dayOfWeek = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
    targetDate = b
    for i in range(a):
        targetDate += dateOfMonth[i]
    print(dayOfWeek[targetDate % 7])

