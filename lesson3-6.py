def capitalize(text):
    return ' '.join(s[:1].upper() + s[1:] for s in text.split(' '))

text = input('Enter a word: ')
print(capitalize(text))
