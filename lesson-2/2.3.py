import yaml

dict_to_yaml = {
    "key_1": [1, 2, 3],
    "key_2": 5,
    "key_3": {
        "1": '\u20ac',
        "2": '\u20bd'
    },
}
with open('data_write.yaml', 'w', encoding='utf-8') as f_n:
    yaml.dump(dict_to_yaml, f_n, default_flow_style=False, allow_unicode=True)

with open('data_write.yaml', encoding='utf-8') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)

print(dict_to_yaml == data)
