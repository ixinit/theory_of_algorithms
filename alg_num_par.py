#!/bin/env python
# -*- coding: utf-8 -*-
import argparse

parser = argparse.ArgumentParser(description='Нумерация пар чисел в N')

parser.add_argument('-x', action="store", dest="x", type=int, help='Назначает x', default=argparse.SUPPRESS)
parser.add_argument('-y', action="store", dest="y", type=int, help='Назначает y', default=argparse.SUPPRESS)

def get_num(x, y):
    if x>=0 and y>=0:
        #number = (max(x,y)+1)**2-1-max(x,y) + (y-x)
        number = max(x,y)**2 - max(x,y) + (y-x)
        print('Номер ({},{}): {}'.format(x,y,number))
    else:
        print('x и y должны быть положительными числами')

if __name__ == '__main__':
    args = parser.parse_args()
    if not vars(args):
        x = int(input("Введите x: "))
        y = int(input("Введите y: "))
        get_num(x, y)
    else:
        get_num(args.x, args.y)
