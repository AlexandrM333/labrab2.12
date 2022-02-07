#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def decorator(tag):
    def wrapper(func):
        def wrapped(old_str):
            low_str = func(old_str)
            result = ["<", tag, ">", low_str, "</", tag, ">"]
            return "".join(result)
        return wrapped
    return wrapper


@decorator(tag="div")
def to_low(old_str):
    low_str = [i.lower() for i in old_str]
    return "".join(low_str)


if __name__ == '__main__':
    to_low_str = input("Введите слова: ")
    print(to_low(to_low_str))
