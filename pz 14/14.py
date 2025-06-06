# В исходном текстовом файле(dates.txt) найти все даты в форматах ДД.ММ.ГГГГ и
# ДД/ММ/ГГГГ. Посчитать количество дат в каждом формате. Поместить в новый
# текстовый файл все даты февраля в формате ДД/ММ/ГГГГ.

with open('dates.txt') as f:
    dates = f.readlines()

dot_count = 0
slash_count = 0
feb_dates = []

for date in dates:
    date = date.strip()
    if len(date) == 10:
        # Проверяем формат ДД.ММ.ГГГГ
        if date[2] == '.' and date[5] == '.':
            dot_count += 1
            day, month, year = date.split('.')
            if month == '02':
                feb_dates.append(f"{day}/{month}/{year}")

        # Проверяем формат ДД/ММ/ГГГГ
        elif date[2] == '/' and date[5] == '/':
            slash_count += 1
            day, month, year = date.split('/')
            if month == '02':
                feb_dates.append(date)


with open('feb_dates.txt', 'w') as f:
    for date in feb_dates:
        f.write(date + '\n')

print(f"Даты ДД.ММ.ГГГГ: {dot_count}")
print(f"Даты ДД/ММ/ГГГГ: {slash_count}")
print(f"Сохранено дат февраля: {len(feb_dates)}")