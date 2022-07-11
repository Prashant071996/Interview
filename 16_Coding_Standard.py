# Need to install flake 8
# After installation in terminal put flake8 file name
# Below is the example


class Student:
    country = "India"

    def __init__(self, rollno, name, std, age):
        self.rollno = rollno
        self.name = name
        self.std = std
        self.age = age

    def display(self):
        print("------------------------------------------------")
        print(f"Name of Student: {self.name}")
        print(f"Roll No        : {self.rollno}")
        print(f"Standard       : {self.std}")
        print(f"Age            : {self.age}")

    @classmethod
    def display_country(cls):
        print(f"Country        : {cls.country}")


s1 = Student("Pratik", 1001, "FY", 22)

s1.display()
s1.display_country()
s2 = Student("Prashant", 1002, "FY", 23)
s2.display()
s2.display_country()
