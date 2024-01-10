#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, endcoding='utf-8') as myfile:
        print(myfile.read())
