class Animal:
    def __init__(self, name: str, sound: str):
        self.name = name
        self.sound = sound

    def speak(self) -> str:
        return f"{self.name} says {self.sound}!"

    def __repr__(self) -> str:
        return f"Animal(name={self.name!r}, sound={self.sound!r})"


if __name__ == "__main__":
    dog = Animal("Dog", "Woof")
    cat = Animal("Cat", "Meow")

    print(dog.speak())
    print(cat.speak())
