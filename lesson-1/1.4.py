array_of_strings = ['разработка', 'администрирование', 'protocol', 'standard']

for word in array_of_strings:
    print(type(word))
    s = word.encode('utf-8')
    print(type(s))
    s = s.decode('utf-8')
    print(type(s))
    print('============')
