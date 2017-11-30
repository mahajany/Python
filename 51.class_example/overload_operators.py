###@total_ordering
class Student:
    def __init__(self, lastname="", firstname=""):
        self.lastname=lastname
        self.firstname=firstname
    def __str__(self):
        return self.lastname + "," + self.firstname
    def __eq__(self, other):
        return ((self.lastname.lower(), self.firstname.lower()) ==
                (other.lastname.lower(), other.firstname.lower()))
    def __lt__(self, other):
        return ((self.lastname.lower(), self.firstname.lower()) <
                (other.lastname.lower(), other.firstname.lower()))
s1=Student("Steve", "Jobs")
s2=Student("Elon", "Musk")
s3=Student("Elon", "Musk")
def check(s1,s2):
    if s1 < s2:
        print(str(s1) + "  <  " + str(s2))
    elif s1 > s2:
        print(str(s1) + "  >  " + str(s2))
    else:
        print(str(s1) + "  ==  " + str(s2))
        print(s1 == s2)
     
  
if __name__=="__main__":
    check(s1,s2)
    check(s2,s1)
    check(s2,s3)
    check(s2,s2)
