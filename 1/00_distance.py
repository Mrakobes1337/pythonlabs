#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
def gay(a,b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

distances = {}

for key in sites.keys():
    distances[key]={}
    for z in sites.keys():
        if z!=key:
            distances[key][z]=gay(sites[key],sites[z])



# TODO здесь заполнение словаря

print(distances)




