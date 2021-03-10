#44. Создать (не программно) текстовый файл со следующим содержимым:
#One — 1 Two — 2 Three — 3 Four — 4
#Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
#При этом английские числительные должны заменяться на русские.
#Новый блок строк должен записываться в новый текстовый файл.

from googletrans import Translator
with open("textfile4_translate.txt", "w", encoding="utf-8") as f:
    with open("eng_words.txt", "r", encoding="utf-8") as f1:
        text = f1.read()
    try:
        f.write(Translator().translate(text, dest='ru').text)
    except AttributeError:
        print('Повторите')
