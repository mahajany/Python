from employee import Employee
from human import *

class ContractEmployee(Employee, Human):
   def  __init__(self, name, salary, duration, height, weight):
        Employee.__init__(self, name,salary)
        Human.__init__(self, height,weight)
        self.duration=duration
   def displayEmployee(self):
     super().displayEmployee()
     super().displayHuman()
     print("...and duration is:", self.duration ," months")
