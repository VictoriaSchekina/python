def my_func(x, y):
    result = 1
    for i in range(abs(y)):
        result *= x
    if y >= 0:
        return result
    else:
        return 1 / result
print(my_func(float(input('Введите первое число: ')), int(input('Введите второе число, отрицательное (степень): '))))
