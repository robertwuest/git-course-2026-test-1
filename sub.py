from main import Animal

# Concrete animal class
class Human(Animal):
    def __init__(self, name: str):
        super().__init__(name, sound="Hello")

    def speak(self) -> str:
        return f"{self.name} says {self.sound}!"

    def __repr__(self) -> str:
        return f"Human(name={self.name!r})"


if __name__ == "__main__":
    h = Human("Alice")
    print(h.speak())
