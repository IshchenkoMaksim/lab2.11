#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Используя замыкания функций, объявите внутреннюю функцию,
# которая бы все повторяющиеся символы заменяла одним другим
# указанным символов. Какие повторяющиеся символы искать и
# на что заменять, определяются параметрами внешней функции.
# Внутренней функции передается только строка для преобразования.
# Преобразованная (сформированная) строка должна возвращаться
# внутренней функцией. Вызовите внутреннюю функцию замыкания
# и отобразите на экране результат ее работы

import re


def main(replaceable, replacement):
    def replace(rep_str):
        if replacement == '' or replaceable == '' or rep_str == '':
            return None

        return re.sub(rf'({replaceable})\1+', replacement, rep_str)

    return replace


if __name__ == '__main__':
    replaceable_s = input("Введите заменяемый символ: ")
    replacement_s = input("Введите заменяющий символ: ")
    string = input("Введите строку: ")
    func_rep = main(replaceable_s, replacement_s)
    print(func_rep(string))
