import os
import sys
if len(sys.argv)<2:
    print("Invalid usage: A directory name was expected")
    sys.exit()
new_dir=sys.argv[1]
dir_name=os.getcwd()
print("Current Working Directory:", dir_name)
try:
    os.chdir(new_dir)
    print("Now changed to:",os.getcwd())
    for f in os.listdir(os.getcwd()):
         print(f)
except:
    print("Failed to change directory to", new_dir)
