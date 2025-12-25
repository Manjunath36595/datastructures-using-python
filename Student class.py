class Student:
    def __init__(self, name, id, branch):
        self.name = name
        self.id = id
        self.branch = branch
    def attend_class(self):
        print("Attending the class")
    def bunk_class(self):
        print("Bunking the class")
    def write_exams(self):
        print("Writing the exams")
s1 = Student("Manju", "A6", "CSE")
print(s1.name)
print(s1.id)
print(s1.branch)



"""
OUTPUT:

Manju
A6
CSE


"""
