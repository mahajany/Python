import os
def debug_py(DebugLevel, DebugString):
    PY_DEBUGGING_LEVEL=int(os.environ.get('PYDEBUG',0))
    
    if PY_DEBUGGING_LEVEL==0: 
        return (1)

    if (  ( DebugLevel == 1 and PY_DEBUGGING_LEVEL == 1 )
       or ( DebugLevel <= 2 and PY_DEBUGGING_LEVEL == 2 )
       or ( DebugLevel <= 3 and PY_DEBUGGING_LEVEL == 3 )):
       print ( DebugString)
    return (0)
