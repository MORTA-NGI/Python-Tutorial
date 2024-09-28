
#Inheritance 
from person import Person


class Employee(Person):
    def __init__(self, name, age, address):
        super().__init__(name, age, address)




person1=Employee('Adam', 25, 'Musgrave')# You need to create an object to use the class
person2=Employee('Sara', 25, 'Musgrave')
person3=Employee('Joe', 25, 'Musgrave')

print(person1.speak("Child can speak as well"))
print(person1.work("Child might not  work"))

print('the person name is ',person1.name)
print('His/her age is ', person1.age)
print('His/her address is ', person1.address)

print ('-----------------------------------------------')
print('the person name is ',person2.name)
print('His/her age is ', person2.age)
print('His/her address is ', person2.address)

print ('-----------------------------------------------')
print('the person name is ',person3.name)
print('His/her age is ', person3.age)
print('His/her address is ', person3.address)



