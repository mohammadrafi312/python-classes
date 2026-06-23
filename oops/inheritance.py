# single inheritance is a feature of object-oriented programming where a class (called a child or subclass) can inherit attributes and methods from another class (called a parent or superclass). This allows for code reusability and the creation of a hierarchical relationship between classes.

class Animal:
    def sound(self):
        print("Animal makes sound")
class dog(Animal):
    pass
    # def sound(self):
    #     print("bark")
d1=dog()
d1.sound()


#multiple inheritance is a feature of object-oriented programming where a class can inherit
class Father:

    def skills(self):
        print("Driving")

class Mother:

    def talent(self):
        print("Cooking")

class Child(Father, Mother):
    pass

c = Child()

c.skills()
c.talent()


#multi level inheritance is a feature of object-oriented programming where a class can inherit
class Animal:

    def sound(self):
        print("Animal Sound")

class Dog(Animal):

    def bark(self):
        print("Bark")

class Puppy(Dog):
    pass

p = Puppy()

p.sound()
p.bark()
# hierarchical inheritance is a feature of object-oriented programming where a class can inherit

# Base class
class Parent:
    def func1(self):
        print("This function is in parent class.")

# Derived class 1
class Child1(Parent):
    def func2(self):
        print("This function is in child 1.")

# Derived class 2
class Child2(Parent):
    def func3(self):
        print("This function is in child 2.")

# Driver code
object1 = Child1()
object2 = Child2()

object1.func1()
object1.func2()
object2.func1()
object2.func3()

#hybrid inheritance is a feature of object-oriented programming where a class can inherit
# Base class
class School:
    def func1(self):
        print("This function is in school.")

# Derived class 1 (Single Inheritance)
class Student1(School):
    def func2(self):
        print("This function is in student 1.")

# Derived class 2 (Another Single Inheritance)
class Student2(School):
    def func3(self):
        print("This function is in student 2.")

# Derived class 3 (Multiple Inheritance)
class Student3(Student1, School):
    def func4(self):
        print("This function is in student 3.")

# Driver code
obj = Student3()
obj.func1()
obj.func2()