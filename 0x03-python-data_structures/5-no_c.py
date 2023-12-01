#!/usr/bin/python3

def no_c(my_string):
    _str = ''
    for i in my_string:
        if i != 'c' and i != 'C':
            _str += i
            return (_str)
