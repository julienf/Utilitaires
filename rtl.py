#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys

message = input("Message: ")

print("Args: ", sys.argv) # Which method is better? argparse/getopt mais c'est pour des options complexes

inverted = ""

for i in range(len(message) - 1, -1, -1): # un peu cracra, pourquoi il faut aller jusqu'à -1 dans le range ?
    inverted += message[i]

print(inverted)

