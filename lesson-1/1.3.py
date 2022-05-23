array_of_strings = ['attribute', 'класс', 'функция', 'type']

for _ in array_of_strings:
    try:
        s = eval(f"b'{_}'")
        print(s)
    except SyntaxError:
        print(f'строку "{_}" невозможно записать в байтовом типе')
