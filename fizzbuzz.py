numbers = []

for i in range(1000, 20001):
    if i % 3 == 0 and i % 5 == 0:
      numbers.append(i)

print(sum(numbers))