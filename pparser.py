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
all_list = []
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
            all_list.append(vars.group(1))
            print('%04i: Local variable: %s = %s' % (n, vars.group(1), vars.group(3).strip(';')))
        for i in all_list:
            if getword(i)(line):
                dictionary.setdefault(i, []).append(n)
    print("\n\tUsage of global variables:")
    for x in dictionary:
        if len(dictionary[x]) > 1:
            print("%s : %s" % (x, dictionary[x][1:]))


##################
# PYTHON PARSER  #
##################

py_fun = re.compile('def\s*?([a-zA-Z_][a-zA-Z0-9_]*\(.*\))')
shebang = re.compile('^#!(.*$)')
encoding = re.compile(".*coding[:=]\s*([-\w.]+)")
py_var = re.compile('([a-zA-Z_][a-zA-Z0-9_]*).?=(.*\n)')

pyvar_list = []
pydictionary = {}


def py_scan(file):
    print("\tGlobal variables:")
    for n, line in enumerate(open(file), 1):
        fun = py_fun.match(line)
        sheb = shebang.match(line)
        cod = encoding.match(line)
        var = py_var.match(line)
        if sheb:
            print("%04i: Shebang: %s" % (n, sheb.group(1)))
        if cod:
            print("%04i: Encoding: %s" % (n, cod.group(1)))
        if fun:
            print("%04i: Function: %s" % (n, fun.group(1)))
        if var:
            pyvar_list.append(var.group(1))
            definition = re.sub(r'(\s#.*)?\n', '', var.group(2))
            print("%04i: Variable: %s =%s" % (n, var.group(1), definition))
        for i in pyvar_list:
            if getword(i)(line):
                pydictionary.setdefault(i, []).append(n)
    print("\n\tGlobal variables usage:")
    for x in pydictionary:
        if len(pydictionary[x]) > 1:
            print("%s : %s" % (x, pydictionary[x][1:]))



def main():
    if len(argv) != 2:
        exit("Usage: ./main.py file{.c|.py}")
    if argv[1].endswith('.c'):
        print("Now parsing your C file...\n")
        scan(argv[1])
    elif argv[1].endswith('.py'):
        print("Now parsing your PYTHON file...\n")
        py_scan(argv[1])
    else:
        exit("Please use a C file (.c) or a PYTHON file (.py)")


if __name__ == "__main__": main()