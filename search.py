#!/usr/bin/env python

 # Krix Apolinario - krix@krix.com.br

from re import compile
from sys import argv, exit

if open('rquivo.txt', 'r') == "@":
    if len(argv) != 3:
        print ('Usage: %s  ' % argv[0])
        exit(1)

        String = argv[1]
        File = argv[2]

        try:
            FileSearch = open(File, 'r')
            ReadingFile = FileSearch.read()
            ReadingFile = ReadingFile.split('n')
            StringSearching = compile(String)
            for Line in ReadingFile:
                FoundString = StringSearching.search(Line)
                if (FoundString):
                    print (Line)
            FileSearch.close()
            exit(0)
        except IOError:
            print ('Oooops... Falhou...')
            exit(2)