#Tuples
print ("========================================================")
print("TUPLES - with paranthesis - ()")
months = ('January','February','March','April','May','June',\
'July','August','September','October','November','  December')
print(months)
#Lists
print ("========================================================")
print("LISTS - with Square-brackets - []")
cats = ['Tom', 'Snappy', 'Kitty', 'Jessie', 'Chester']
print("cats[2]:", cats[2])
print("cats:", cats)
cats.append('Catherine')
print("cats, after append(Catherine)", cats)
del cats[1]
print("cats: after del cats[1]:", cats)

#Dictionary:
print ("========================================================")
print("DICTIONARIES - with curly braces - []")
phonebook = {'Andrew Parson':8806336, \
'Emily Everett':6784346, 'Peter Power':7658344, \
'Lewis Lame':1122345}
print("phonebook:" , phonebook )
phonebook['Gingerbread Man'] = 1234567
print("phonebook, with new entry:", phonebook )
del phonebook['Andrew Parson']
print("phonebook, after deleting a name:", phonebook )
