#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence != '':
        first_charcter = sentence[0]
    else:
        first_charcter = None
    return (len(sentence), first_charcter)
