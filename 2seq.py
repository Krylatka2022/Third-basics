"""5. (МОДУЛЬ 2) создать модуль 2seq.py. Задание:
Пользователь вводит любые цифры через запятую
Сохранить цифры в список
Получить новый список в котором будут только уникальные элементы исходного (уникальным считается символ, который встречается в исходном списке только 1 раз)
Вывести новый список на экран
Порядок цифр в новом списке не важен
Пример работы: Введите элементы списка через запятую: 2,3,4,5,5,6,5,3,9
Результат: 2, 4, 6, 9

(Дополнительно*) Предусмотреть что пользователь может использовать один из 3-х разделителей:
запятую, точку с запятой, слэш (1,2,3 1;2;3 1/2/3), но только какой то один 1,2;3/4 - так нельзя
"""
user_input = input("Введите элементы списка через запятую: ")

# Основное задание
numbers = user_input.split(',')
numbers = [int(num) for num in numbers]

frequency = {num: numbers.count(num) for num in numbers}
unique_numbers = [num for num, count in frequency.items() if count == 1]

print("Результат:", ", ".join(map(str, unique_numbers)))

# Дополнительно (*)
user_input = input("Введите элементы списка через запятую, точку с запятой или слэш: ")

separators = {',', ';', '/'}
used_separators = [sep for sep in separators if sep in user_input]

if len(used_separators) == 1:
    separator = used_separators[0]
    numbers = user_input.split(separator)
    numbers = [int(num) for num in numbers]

    frequency = {num: numbers.count(num) for num in numbers}
    unique_numbers = [num for num, count in frequency.items() if count == 1]

    print("Результат (дополнительно):", ", ".join(map(str, unique_numbers)))
else:
    print("Так нельзя: используйте только один тип разделителя.")
