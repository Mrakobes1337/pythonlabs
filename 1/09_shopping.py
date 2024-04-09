#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь магазинов с распродажами

shops = {
    'ашан':
        [
            {'name': 'печенье', 'price': 10.99},
            {'name': 'конфеты', 'price': 34.99},
            {'name': 'карамель', 'price': 45.99},
            {'name': 'пирожное', 'price': 67.99}
        ],
    'пятерочка':
        [
            {'name': 'печенье', 'price': 9.99},
            {'name': 'конфеты', 'price': 32.99},
            {'name': 'карамель', 'price': 46.99},
            {'name': 'пирожное', 'price': 59.99}
        ],
    'магнит':
        [
            {'name': 'печенье', 'price': 11.99},
            {'name': 'конфеты', 'price': 30.99},
            {'name': 'карамель', 'price': 41.99},
            {'name': 'пирожное', 'price': 62.99}
        ],
}

# Создайте словарь цен на продкты следующего вида (писать прямо в коде)
# TODO тут с клавиатуры введите магазины и цены (можно копипастить ;)
sweets = {
    'название сладости': [
        {'shop': 'название магазина', 'price': 99.99},
    ],
    # TODO тут с клавиатуры введите другую сладость и далее словарь магазинов
}
sweets={}
for key in shops.keys():
    for prod in shops[key]:
        if prod["name"] not in sweets.keys():
            sweets[prod["name"]]=[]
        sweets[prod["name"]].append({"shop":key,"price":prod["price"]})
print(sweets)

# Указать надо только по 2 магазина с минимальными ценами

for key in sweets.keys():
    maxs=max([sweets[key][x]["price"] for x in range(len(sweets[key]))])
    for x in sweets[key]:
        if x["price"]==maxs:
            sweets[key].remove(x)
print(sweets)
        
        



