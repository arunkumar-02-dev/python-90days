class Student:
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

# creating object
s1 = Student()

# assigning values manually
s1.name = "Arun"
s1.age = 21

# calling method
s1.display()
