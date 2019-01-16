#1475

num = input()
cnt = []
cnt.append(num.count('0'))
cnt.append(num.count('1'))
cnt.append(num.count('2'))
cnt.append(num.count('3'))
cnt.append(num.count('4'))
cnt.append(num.count('5'))
cnt.append(int((num.count('6') + num.count('9')+1)/2))
cnt.append(num.count('7'))
cnt.append(num.count('8'))

print(max(cnt))