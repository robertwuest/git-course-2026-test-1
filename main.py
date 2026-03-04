class Animal:
    def __init__(self, name: str, sound: str, category: str) -> None:
        self.name = name
        self.sound = sound
        self.category = category

    def speak(self) -> str:
        return f"{self.name} says {self.sound}!"
    
    def roar(self) -> str:
        return f"ASEOIDFASPOIDJAWSDPAOISW"

    def __repr__(self) -> str:
        return f"Animal(name={self.name!r}, sound={self.sound!r}, category={self.category!r})"


if __name__ == "__main__":
    dog = Animal("Dog", "Woof", "Mammal")
    cat = Animal("Cat", "Meow", "Mammal")

    print(dog.speak())
    print(cat.speak())
