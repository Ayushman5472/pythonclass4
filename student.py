class Student (object):
    def __init__(self,name,age,gender,level):
        self.name = name
        self.age = age
        self.gender = gender
        self.level = level
        self.grades = {}
    
    def setGrade(self, course, grade):
        self.grades [course] = grade
    
    def getGrade(self, course):
        return(
            self.grades[course]
        )
    
    def getTotal(self):
        return(
            sum(self.grades.values())
        )

Ayush = Student("Ayushman", 14, "Male", "8")
print(Ayush.name)
Ayush.setGrade("math", 95)
Ayush.setGrade("Science", 95)
print(Ayush.getTotal())

Student2 = Student("name", 14, "Male", "8")
Student2.setGrade("math", 10)
Student2.setGrade("Science", 90)
print(Student2.getTotal())