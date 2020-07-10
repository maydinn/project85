class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def output(self):
        print(self.name, self.surname, self.age)


student = Person("adem", "tatlı", 27)

teacher = Person("Nehring", "Schumacher", 43)

print(student.surname)
print(teacher.name)

student.output()
teacher.output()