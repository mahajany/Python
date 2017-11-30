import os
print (os.environ['PATH'])
print(os.environ['HOME'])

#os.environ['scripting']


sorted_env = os.environ.keys()
sorted(sorted_env)
for key in sorted_env:
    print ('%s = %s' % (key, os.environ[key]))
