def person(name, surname, year, city, email, phone):
    result = f'{name} {surname}, {year} year of birth, from {city}, {email}, {phone}'
    return result

print(person('Adam', 'Shmidt', '1991', 'Tel-Aviv', 'mail@mail.com', '+49123456'))
