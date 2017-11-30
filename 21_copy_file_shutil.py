#!/bin/usr/python3
import sys
import shutil
in_file_name = sys.argv[1]
out_file_name = sys.argv[2]
shutil.copy(in_file_name, out_file_name)

