#!/usr/bin/env python

import random
import os

def getQuotes():
    dirloc = os.path.dirname(os.path.realpath(__file__))
    quoteloc = dirloc + '/quotes.txt'
    quotes = []
    with open (quoteloc) as f:
        for line in f:
            quotes.append(line)
        f.closed
    return quotes

def printQuotes(quotes):
    print("Ça va")
    print(quotes[random.randint(0,len(quotes)-1)])

printQuotes(getQuotes())
