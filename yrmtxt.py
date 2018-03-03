#!/usr/bin/env python3.6

from sys import argv

script, filename = argv

#open file
target = open(filename, 'w')

#delete all text
print("""Truncating the file...
Done.
""")
target.truncate()

#close file
target.close()
