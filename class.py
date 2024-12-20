class Person_KhalidEhab:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def print(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"City: {self.city}")

person = Person_KhalidEhab("Khalid Ehab", 21, "Sadat City")

person.print()
