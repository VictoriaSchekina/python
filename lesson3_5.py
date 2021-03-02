while True:
    numbers = input('Введите числа: ')
    numbers_list = numbers.split(' ')
    if numbers == '&':
        break
        print(int_numbers_list)
    else:
        int_numbers_list = map(int, numbers_list)
        print(sum(int_numbers_list))
        continue

#программа выдает сумму и останавливается при написании символа &,
#но я не знаю как сделать так, чтобы она добавляла сумму к существующему результату