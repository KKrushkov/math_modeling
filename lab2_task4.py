n = int(input())
a = 1
b = 1
i = 0
x = [1, 1]
while i < n-2:
    f = a + b
    x.append(f)
    a = b
    b = f
    i += 1
print(''.join([str(i) for i in x]))
    