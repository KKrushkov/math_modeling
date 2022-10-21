x = int(input())
y = int(input())

if y == 0:
    print("Ты дурачок, на 0 делить нельзя")
elif x % y == 0:
    print("Делится без остатка")
    print("Частное:", x / y)
else:
    print("Нацело не делится")
    print("Остаток:", x % y)
    print("Частное:", x / y)