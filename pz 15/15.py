import sqlite3


conn = sqlite3.connect('tv_repair.db')
cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS repairs (
    brand TEXT,
    manufacturer TEXT,
    price REAL,
    repair_date TEXT,
    document TEXT,
    master TEXT,
    payment REAL
)
''')
conn.commit()


# добавления записи
def add_repair():
    print("\nДобавление нового ремонта:")
    data = (
        input("Марка телевизора: "),
        input("Завод-изготовитель: "),
        float(input("Цена телевизора: ")),
        input("Дата ремонта (ГГГГ-ММ-ДД): "),
        input("Номер документа: "),
        input("ФИО мастера: "),
        float(input("Сумма оплаты: "))
    )
    cursor.execute('INSERT INTO repairs VALUES (?,?,?,?,?,?,?)', data)
    conn.commit()
    print("Запись добавлена!\n")


# Функция для поиска записей
def find_repairs():
    print("\nВарианты поиска:")
    print("1 - По марке телевизора")
    print("2 - По мастеру")
    print("3 - По дате ремонта")
    choice = input("Выберите вариант: ")

    if choice == '1':
        brand = input("Введите марку: ")
        cursor.execute("SELECT * FROM repairs WHERE brand=?", (brand,))
    elif choice == '2':
        master = input("Введите мастера: ")
        cursor.execute("SELECT * FROM repairs WHERE master=?", (master,))
    elif choice == '3':
        date = input("Введите дату (ГГГГ-ММ-ДД): ")
        cursor.execute("SELECT * FROM repairs WHERE repair_date=?", (date,))

    results = cursor.fetchall()
    print("\nНайдено записей:", len(results))
    for row in results:
        print(row)


# Функция для редактирования записи
def edit_repair():
    print("\nРедактирование записи")
    doc_num = input("Введите номер документа для поиска: ")
    cursor.execute("SELECT * FROM repairs WHERE document=?", (doc_num,))
    repair = cursor.fetchone()

    if repair:
        print("Найдена запись:", repair)
        field = input("Какое поле меняем (brand/manufacturer/price/...)? ")
        new_value = input("Новое значение: ")
        cursor.execute(f"UPDATE repairs SET {field}=? WHERE document=?", (new_value, doc_num))
        conn.commit()
        print("Запись обновлена!")
    else:
        print("Запись не найдена")


# удаления записи
def delete_repair():
    print("\nУдаление записи")
    print("1 - Удалить по номеру документа")
    print("2 - Удалить по марке телевизора")
    print("3 - Удалить по мастеру")
    choice = input("Выберите вариант: ")

    if choice == '1':
        doc_num = input("Введите номер документа: ")
        cursor.execute("DELETE FROM repairs WHERE document=?", (doc_num,))
    elif choice == '2':
        brand = input("Введите марку телевизора: ")
        cursor.execute("DELETE FROM repairs WHERE brand=?", (brand,))
    elif choice == '3':
        master = input("Введите мастера: ")
        cursor.execute("DELETE FROM repairs WHERE master=?", (master,))

    conn.commit()
    print("Удалено записей:", cursor.rowcount)


# Главное меню
while True:
    print("\nТЕЛЕМАСТЕРСКАЯ - Учет ремонтов")
    print("1 - Добавить ремонт")
    print("2 - Найти ремонт")
    print("3 - Редактировать запись")
    print("4 - Удалить запись")
    print("5 - Выход")

    choice = input("Выберите действие: ")

    if choice == '1':
        add_repair()
    elif choice == '2':
        find_repairs()
    elif choice == '3':
        edit_repair()
    elif choice == '4':
        delete_repair()
    elif choice == '5':
        break

conn.close()