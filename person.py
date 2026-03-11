class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        return f"Hello, my name is {self.name} and I'm {self.age} years old."
    
    def birthday(self):
        self.age += 1
        return f"Happy birthday! {self.name} is now {self.age}."
