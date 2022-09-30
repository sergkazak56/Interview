import re
from stack import Stack

DICT_PARSS = {'(':')', '[':']', '{':'}'}

TEXT1 = "К нему подвели {чистокровного жеребца [его зовут Огонёк], который обещает стать} чемпионом на скачках."
TEXT2 = "С реки повеяло ночной {прохладой ((солнце еще не взошло)) и какой-то промозглой} сыростью и( запахом тины."
TEXT3 = "На (мельнице дедушка {показал мне специальный деревянный) [ящик, (как говорят) ларь,] для хранения муки"
TEXT4 = "К нему подвели чистокровного жеребца его зовут Огонёк, который обещает стать чемпионом на скачках."
TEXT5 = "[([])((([[[]]])))]{()}"
TEXT6 = "{{[(])]}}"

def change_text(text, simbol):
    """
    Функция замены парных скобок в тексте на символ *
    :param text: входной текст
    :param simbol: одна из открывающихся скобок
    :return: изменненный текст
    """
    rslice = text[text.rindex(simbol):]
    rslice = rslice.replace(simbol, '*')
    rslice = rslice.replace(DICT_PARSS[simbol], '*', 1)
    lslice = text[:text.rindex(simbol)]
    return lslice + rslice

def find_in_text(text, position1, rparss =''):
    """
    Функция ставит в исходном тексте указатели ---> <---, которые указывают на непарные скобки(у)
    :param text: исходный текст
    :param position1: позиция первой непарной скобки
    :param rparss: вторая непарная скобка, если таковая есть
    :return: измененный текст с указателями на  непарные скобки(скобку)
    """
    if not rparss:
        return text[:position1] + '   --->' + text[position1:position1 + 1] + '<---   ' + text[position1 + 1:]
    else:
        position2 = position1 + text[position1:].index(rparss)
        pass
        return text[:position1] + '   --->' + text[position1:position2 + 1] + '<---   ' + text[position2 + 1:]

def check_parentheses(text):
    """
    Функция поиска непарных скобок в тексте
    :param text: исходный текст
    :return: кортеж, первым элементом которого является значение типа boolean
             True - все скобки парные или скобок в тексте нет
             False - непарные скобки в тексте имеются
    """
    regexp_str = ''
    for key, value in DICT_PARSS.items():
        regexp_str += f'\\{key}|\\{value}|'
    regexp_str = regexp_str.rstrip('|')
    find_str = re.findall(regexp_str, text)
    if not find_str:
        return True, 'Скобок в тексте не найдено'
    s_output = Stack()
    s_receive = Stack()
    for item in find_str:
        s_output.push(item)
    while True:
        if s_output.peek() in DICT_PARSS.values():
            s_receive.push(s_output.pop())
        elif s_output.peek() in DICT_PARSS.keys():
            parss = DICT_PARSS[s_output.peek()]
            if s_receive.peek() and s_receive.peek() == parss:
                s_receive.pop()
                text = change_text(text, s_output.pop())
            else:
                break
        else:
            break
    if s_output.isEmpty() and s_receive.isEmpty():
        return True, 'Все скобки в тексте парные'
    elif not s_output.isEmpty() and s_receive.isEmpty():
        return False, s_output.peek(), text.rindex(s_output.peek()), ''
    elif s_output.isEmpty() and not s_receive.isEmpty():
        return False, s_receive.peek(), text.index(s_receive.peek()), ''
    elif not s_output.isEmpty() and not s_receive.isEmpty():
        return False, s_output.peek(), text.rindex(s_output.peek()), s_receive.peek()

def print_result(text):
    """
    Функция вывода результатов поиска непарных скобок в консоль
    :param text: исходный текст
    :return:    1. исходный текст
                2. обнаружены или не обнаружены непарные скобки(а) и, начиная с какой позиции в тексте
                3. в случае обнаружения скобок(ки), выводит текст с указателями на напарные скобки(у)
    """
    print(f'ВХОДНОЙ ТЕКСТ: {text}')
    res_tuple = check_parentheses(text)
    if not res_tuple[0]:
        print(f'{" " * 15}Обнаружены непарные скобки {res_tuple[1]},{res_tuple[3]} начиная с позиции {res_tuple[2] + 1}')
        print(" " * 14, find_in_text(text, res_tuple[2], res_tuple[3]))
    else:
        print(" " * 14, res_tuple[1])

def task12():
    """
    Головная функция вызова функций и методов
    :return: выводит результаты в консоль
    """
    # Пример работы стека (задание 1):
    print('Пример работы стека (задание 1):')
    my_str = "Это строка для стека"
    print(my_str)
    my_stack = Stack()
    print(f'my_stack пуст? {my_stack.isEmpty()}')
    print(f'Размер my_stack: {my_stack.size()}')
    print(f'Добавляем элементы в стек')
    for item in list(my_str):
        my_stack.push(item)
    print(f'Теперь размер my_stack: {my_stack.size()}')
    print(f'my_stack: {my_stack}')
    print(f'Удаляем последний элемент стека: {my_stack.pop()}')
    print(f'Теперь размер my_stack: {my_stack.size()}')
    print(f'my_stack: {my_stack}')
    print(f'Последний элемент стека: {my_stack.peek()}')
    dict_ = {'abc':123, 'def':456}
    print(f'Добавляем элемент {dict_} в стек')
    my_stack.push(dict_)
    print(f'Теперь размер my_stack: {my_stack.size()}')
    print(f'my_stack: {my_stack}')
    print(f'Последний элемент стека: {my_stack.peek()}')
    print(f'my_stack пуст? {my_stack.isEmpty()}')
    print()
    print('*' * 30)
    # Проверка скобок на парность (задание 2):
    print('Проверка скобок на парность (задание 2):')
    print_result(TEXT1)
    print_result(TEXT2)
    print_result(TEXT3)
    print_result(TEXT4)
    print_result(TEXT5)
    print_result(TEXT6)
