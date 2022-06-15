def string_to_bit_type(arr):
    for _ in arr:
        bit_type = eval(f"b'{_}'")
        print(bit_type)
        print(type(bit_type))
        print(len(bit_type))
        print('---------')


s1 = 'class'
s2 = 'function'
s3 = 'method'

array_of_strings = [s1, s2, s3]

string_to_bit_type(array_of_strings)
