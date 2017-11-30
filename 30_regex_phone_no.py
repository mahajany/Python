import re
import sys
input_string=sys.argv[1]
pattern=r"^[0-9]{3}[ -]{0,1}[0-9]{3}[ -]{0,1}[0-9]{4}$"
if re.search(pattern, input_string):
   print(input_string, " is a valid phone number") 
else:
   print(input_string, " ----DOES NOT SEEM LIKE A PHONE NUMBER")
