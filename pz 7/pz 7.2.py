#Дана строка-предложение на русском языке. Вывести самое короткое слово в
#предложении. Если таких слов несколько, то вывести последнее из них. Словом
#считать набор символов, не содержащий пробелов, знаков препинания и
#ограниченный пробелами, знаками препинания или началом/концом строки.
def find_word(sentence):
    words = sentence.split()
    min_length = min(len(word) for word in words)

    # Проходимся по словам справа налево и ищем первое подходящее
    for word in reversed(words):
        if len(word) == min_length:
            return word.strip(".,!?;:")  # Убираем возможные знаки препинания

    return

sentence = input("Введите предложение: ")
short_word = find_word(sentence)
print(short_word)