'''
example for the 2th question:
'''

#for operators and
print(bool(5==5 and 7>5)) #True
print(bool(75!=5 and 5>9)) #False

#for or
print(bool(7>=7 or 5!=5)) #True

#for not
x = 5
print(not(x > 3 and x < 10)) #False


'''
example for the 4th question:
'''
class student:
    def __init__(self, name, faculty):
        self.name = name
        self.faculty = faculty
first_student=student("Abdufattokh", "TIF")
print(first_student.name)

'''
example for the 5th question:
'''
class Parent1():
    pass
class Parent2():
    def __init__(self):
        print("Parent2")
class Child(Parent1, Parent2):
    def __init__(self):
        super().__init__()
        print("Child")
        
instance = Child()
print(isinstance(instance, Parent1))
print(isinstance(instance, Parent2))
