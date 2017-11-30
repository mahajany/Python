from employee import Employee
employees=[]
employees.append(Employee("Elon", 1200))
employees.append(Employee("Musk", 2103))
employees.append(Employee ("John",1201))
employees.append(Employee ("Cenna", 1223))
for e in employees:
    e.displayEmployee()
print("Total employee count:"+ str( Employee.empCount))
e=employees[1]
if hasattr(e, 'salary'):
   setattr(e, 'salary', getattr(e,'salary') - 1001 )
   setattr(e, 'bonus', 5001 )
e.displayEmployee()
if hasattr(e, 'bonus'):
  print("Total:",  e.bonus+e.salary)
e.info()
