
from person import Person
class Student (Person):
    def __init__(self, name, age, address, Grade):
        super().__init__(name, age, address)
        self.Grade=Grade

  
    def Marks(self, grade):
        if self.Grade > 50:
            print('You Pass the exam')



student= Student('Adam', 26, 'Musgrave', 80)

print(student.name)
print(student.Grade)
print(student.Marks(student.Grade))