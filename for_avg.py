import numpy as np

a = int(input())
b = int(input())
list = []

for n in range(a, b+1):
    if n%3 == 0:
        list.append(n)

print(np.mean(list))