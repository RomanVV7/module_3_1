# Домашняя работа по уроку "Пространство имён"
# Задача "Счётчик вызовов":
# Порой необходимо отслеживать, сколько раз вызывалась та или иная функция.
# К сожалению, в Python не предусмотрен подсчёт вызовов автоматически.
# Давайте реализуем данную фишку самостоятельно!

calls = 0

def count_calls():
    global calls
    calls = calls + 1

def string_info (string):
    count_calls()
    tuple = len(string), string.upper(), string.lower()
    return tuple

def is_contains(string, list_to_search):
    count_calls()
    for word in list_to_search:
        if string.lower() in word.lower() or word.lower() in string.lower():
            return True
        else:
            return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)