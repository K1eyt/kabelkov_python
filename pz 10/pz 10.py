#Вариант 12.
#В магазинах имеются следующие товары. Магнит – молоко, соль, сахар, печенье, сыр.
#Пятерочка – мясо, молоко, сыр. Перекресток – молоко, творог, сыр, сахар, печенье.
# Лента – печенье, молоко, сыр, сметана.
#Определить:
#1. в каких магазинах нельзя приобрести сметану.
#2. какие товары из магазина Магнит отсутствуют в магазине Перекресток.
#3. какие товары из магазина Лента отсутствуют в магазине Магнит.
magnet = {"молоко", "соль", "сахар", "печенье", "сыр"}
pyaterochka = {"мясо", "молоко", "сыр"}
perekrestok = {"молоко", "творог", "сыр", "сахар", "печенье"}
lenta = {"печенье", "молоко", "сыр", "сметана"}

storesmetana = []
if "сметана" not in magnet:
    storesmetana.append("Магнит")
if "сметана" not in pyaterochka:
    storesmetana.append("Пятерочка")
if "сметана" not in perekrestok:
    storesmetana.append("Перекресток")
if "сметана" not in lenta:
    storesmetana.append("Лента")

a = magnet - perekrestok
b = lenta - magnet

print("Магазины, где нельзя приобрести сметану:", storesmetana)
print("Товары из Магнита, отсутствующие в Перекрестке:", a)
print("Товары из Ленты, отсутствующие в Магните:", b)
