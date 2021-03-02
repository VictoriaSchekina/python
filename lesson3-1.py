def division():
    try:
        a = int(input('Введите первое число: '))
        b = int(input('Введите второе число: '))
        result = a / b
    except ZeroDivisionError:
        return "На ноль делить нельзя"
    return result
print(division())
