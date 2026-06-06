### type 3 глубже

with open('../files/16333.txt', 'r') as f:
    data = f.readline()
'''
for i in 'QRW':
    data = data.replace(i,'a')

data = data.translate(str.maketrans('QRW124','aaa000'))
for i in '124':
    data = data.replace(i,'0')
while 'aa' in data or '00' in data:
    data = data.replace('aa', 'a a').replace('00','0 0')
data = data.split()
print(data)
'''

    ### главный линейный способ
'''
data = data.translate(str.maketrans('QRW124','aaa000'))

max_len = 1
cur_len = 1
for i in range(1,len(data)):
    if data[i] != data[i-1]:
        cur_len +=1
        max_len = max(max_len, cur_len)
    else:
        cur_len = 1
print(max_len)
'''
'''
left = 0
max_len = 0

for right in range(1,len(data)):
    if data[right] == data[right -1]:
     left = right

    cur_len = right - left + 1
    
    max_len = max(max_len, cur_len)
print(max_len)
'''

with open('../files/13866 (1).txt', 'r') as f:
    data = f.readline()

data = data.translate(str.maketrans('13579','*****'))
'''
while '***' in data:
    data = data.replace('***','*1 * 1*')

parts = data.split()

print(parts)
'''

'''
current_len = 2
max_len = 0

for i in range(2,len(data)):
    current_len = current_len + 1
    if data[i] == data[i-1] == data[i-2] =='*':
        current_len = 2

    max_len = max(max_len, current_len)
print(max_len)
'''
#почему 9 и что нужно сделать чтобы исправить ошибку
