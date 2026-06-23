# class dog:#class
#     def __init__(self,fullname):#constructor
#         self.name=fullname
#         print(fullname)#message

# d1=dog("Bud")#object

class student :
    college_name="ABC College"#class variable
    def __init__(self,name,marks):#constructor
        self.name=name#instance variable
        self.marks=marks#instance variable  
    def average(self):#instance method
        return self.marks/2