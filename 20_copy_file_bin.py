#!/bin/usr/python3
import sys
in_file_name = sys.argv[1]
out_file_name = sys.argv[2]
out_file = open(out_file_name, "wb")
with open(in_file_name, "rb") as in_file:
    while True:
        byte = in_file.read(1)
        if not byte:
            break
        ##out_file.write(byte[0])
        out_file.write(byte)


