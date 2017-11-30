from my_modules.hello  import Hello
from my_modules.maths  import MyMaths as mm
from my_modules.mm2.maths  import MyMaths as mm2

import sys
print(sys.path)
Hello.log("Shut up everybody, shut up! Don't move, don't speak, don't breathe, I'm trying to think")
Hello.log(str(22234)+" and "+str(222))
print(mm.add(22234, 222))
print(mm.multiply(22234, 222))
print(mm2.multiply(22234, 222))
