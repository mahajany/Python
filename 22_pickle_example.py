import pickle

a = ['test value','test value 2','test value 3']
print("Pre-pickled-date:")
print(a)
file_Name = "pickle_file.dat"
# open the file for writing
fileObject = open(file_Name,'wb') 

# this writes the object a to the
# file named 'testfile'
pickle.dump(a,fileObject)   

# here we close the fileObject
fileObject.close()
# we open the file for reading
fileObject = open(file_Name,'rb')  
# load the object from the file into var b
b = pickle.load(fileObject)  
print("Un-pickled-data:")
print(b)
if a==b:
    print("a == b - i.e. pre-pickled and un-pickled data is equivalent")

print("Check what is written there: cat pickle_file.dat")
