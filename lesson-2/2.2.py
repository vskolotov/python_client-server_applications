import json


def write_order_to_json(item, quantity, price, buyer, date):
    with open('orders.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    data["orders"].append({
        "item": item,
        "quantity": quantity,
        "price": price,
        "buyer": buyer,
        "date": date
    })

    with open('orders.json', 'w', encoding='utf-8') as f_n:
        json.dump(data, f_n, sort_keys=False, ensure_ascii=False, indent=4)


write_order_to_json('книга', 5, 245, 'Ozon', '20.04.2022')
write_order_to_json('тетрадь', 50, 24, 'Озон', '22.04.2022')
