#2. Из предложенного текстового файла (text18-12.txt) вывести на экран его содержимое,
#количество пробельных символов. Сформировать новый файл, в который поместить текст
#в стихотворной форме предварительно вставив после каждой строки строку из символов
#«*».

# Чтение содержимого файла
with open('text18-12.txt', 'r', encoding='utf-16') as file:
    content = file.read()

# Вывод содержимого файла на экран
print("Содержимое файла:")
print(content)

# Подсчет пробельных символов
space_count = content.count(' ')
newline_count = content.count('\n')
total_whitespace = space_count + newline_count

print(f"\nКоличество пробелов: {space_count}")
print(f"Количество символов переноса строки: {newline_count}")
print(f"Общее количество пробельных символов: {total_whitespace}")

# Создание нового файла с добавлением строк из '*'
lines = content.split('\n')
new_content = []

for line in lines:
    new_content.append(line)
    new_content.append('*' * len(line))  # Строка из '*' той же длины, что и исходная строка

# Объединение строк с переносами
new_content_text = '\n'.join(new_content)

with open('modified_text18-12.txt', 'w', encoding='utf-8') as new_file:
    new_file.write(new_content_text)

print("\nФайл 'modified_text18-12.txt' создан с добавлением строк из '*'.")