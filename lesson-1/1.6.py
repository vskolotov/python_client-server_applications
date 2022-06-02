from chardet import detect

FILE = 'test_file.txt'

with open(FILE, 'rb') as f:
    content = f.read()
encoding = detect(content)['encoding']

with open(FILE, encoding=encoding) as f_n:
    for el_str in f_n:
        print(el_str, end='')
