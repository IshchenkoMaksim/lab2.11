#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    tpl = lambda a, b: (a, b)
    a = tpl(1, 2)
    b = tpl(3, a)
    c = tpl(a, b)
    print(f"a = {a}\nb = {b}\nc = {c}")
