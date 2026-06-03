'''
data = 'ABCAABACACAB'
data = data.replace('AB', 'A B')
data = data.split()
answer = max([len(x) for x in data])
answer = max(data, key = len)
print(data,len(answer))
'''
#map(func, data) #примняет функци ю func к кадлому элементу data
#################задача 1 способ 1
'''
with open('../files/2401.txt') as f:
    data = f.readline()
    #делим по сигменту
    data = data.replace('ad', 'a d').replace('da', 'd a')
    answer = len(max(data.split(), key = len))
    print(answer)
'''
##############3адача 1 способ 2
'''
with open('../files/2401.txt') as f:
    data = f.readline()
cur = 1
max_len = 0
for i in range(len(data)-1):
    if data[i] + data[i + 1] in ('ad', 'da'):
        cur = 1
    else:
        cur += 1
    max_len = max(cur, max_len)
print(max_len)
'''