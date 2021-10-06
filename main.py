#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# Catches global variables, local variables, functions, followed with their usage line number.

import re
from sys import argv

#############
# C PARSER  #
#############

cdef = re.compile('[ \t]*#[ \t]*define[ \t]+(\S+)[ \t]*((?:.*\\\r?\n)*.*)', re.MULTILINE|re.DOTALL)
comm = re.compile('/\*[^*]*\*+(?:[^/*][^*]*\*+)*/', re.MULTILINE)
incl = re.compile('^[ \t]*#[ \t]*include[ \t]*["<]([^">]+)*[">]', re.MULTILINE)

var = re.compile('(?:\w+\s+)([a-zA-Z_][a-zA-Z0-9_]*)(.?=)(.*?;)', re.MULTILINE)
slash = re.compile(r'.*\\$')
curly_open = re.compile('.*?({)')
curly_close = re.compile('.*?(})')
fun = re.compile('(?:\w+\s+)([a-zA-Z_][a-zA-Z0-9_ ]*\(.*\).*{)')

var_list = []
sym_list = []
all_liste = []
dictionary = {}

# getword will catch all variables used inside brackets
def getword(word):
    return re.compile(r'\b({0})\b'.format(word)).search

def scan(file) :
    count=0
    next_line = None
    print("\tGlobal variables:")
    for n, line in enumerate(open(file), 1) :
        matched = cdef.match(line)
        includes = incl.match(line)
        funs = fun.match(line)
        vars = var.match(line)
        if next_line:
            line = re.compile(r'([^\\]*)').match(next_line).group(1) + line
            matched = cdef.match(line)
            next_line=None
        if (slash.match(line)):
            next_line = line
            continue
        if matched :
            symbol = matched.group(1)
            definition = re.sub(r'/\*[^*]*\*+(?:[^/*][^*]*\*+)*/', '', matched.group(2)) # removes comments
            all_list.append(symbol)
            print('%04i: Global variable: %s = %s' % (n, symbol, definition.strip('\n')))
        if includes:
            print('%04i: Included file: %s' % (n, includes.group(1)))
        if funs:
            print('%04i: Function: %s' % (n, funs.group(0).strip('{')))
        if vars:
            all_liste.append(vars.group(1))
            print('%04i: Local variable: %s = %s' % (n, vars.group(1), vars.group(3).strip(';')))
        for i in all_liste:
            if getword(i)(line):
                dictionary.setdefault(i, []).append(n)
    print("\n\tUsage of global variables:")
    for x in dictionary:
        if len(dictionary[x]) > 1:
            print("%s : %s" % (x, dictionary[x][1:]))


def main():
    if len(argv) != 2:
        exit("Usage: ./main.py file.c")
    if argv[1].endswith('.c'):
        print("Now parsing your file...\n")
        scan(argv[1])
    else:
        exit("Please use a C file (.c)")


if __name__ == "__main__": main()