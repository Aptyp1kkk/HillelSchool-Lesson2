a = int(input("Введите любое число: "))
b = 0
while a > 0:
    float = a % 10
    a = a // 10
    b = b * 10
    b = b + float
print('"Обратное"число:', b)