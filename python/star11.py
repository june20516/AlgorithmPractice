n = int(input())

def makeTop(lst):
    result = []
    for i in range(len(lst)):
        result.append('{}'.format(' '*len(lst)) + lst[i] + '{}'.format(' '*len(lst)))
    return result

def makeBot(lst):
    result = []
    for i in range(len(lst)):
        result.append(lst[i] +' '+ lst[i])
    return result

def line(lst):
    top = makeTop(lst)
    bot = makeBot(lst)
    return top + bot

star = ['  *  ',' * * ','*****']
idx = [3]

for i in range(10):
    idx.append(idx[i]*2)

for i in range(idx.index(n)):
    star = line(star)

for i in range(len(star)):
    print(star[i])
