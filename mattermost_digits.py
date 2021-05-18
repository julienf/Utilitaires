#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys

# print("Argsx: ", sys.argv) # Which method is better? argparse/getopt mais c'est pour des options complexes

toString = str(sys.argv[1])

dicoWords = {"0": ":zero:", "1": ":one:", "2": ":two:", "3": ":three:", "4": ":four:", 
        "5": ":five:", "6": ":six:", "7": ":seven:", "8": ":eight:", "9": ":nine:", ".": "."}

output = ""

for i in range(len(toString)):
    output += dicoWords[toString[i]]

print(output)

