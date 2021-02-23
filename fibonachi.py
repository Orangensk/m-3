n1 = n2 = 1
data = [n1,n2]
for i in range(1, 40):
    tmp = n1 + n2
    if tmp >= 10000000:
        break
    else:
        n1 = n2
        n2 = tmp
        data.append(tmp)

data1 = []
for j in data:
    if j % 2 == 0:
        data1.append(j)


print('\nКоличество элементов в последовательности: ' + str(len(data)) + '\n')
print('Cумма четных элементов: ' + str(sum(data1)) + '\n')
print('Четные элементы:\n' + str(data1) + '\n')
print('Предпоследнее число последовательности: ' + str(data[-2]) + '\n')

