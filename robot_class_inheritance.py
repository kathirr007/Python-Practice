class Robot:
    def __init__(self, name):
        self.name = name
        self.position = [0, 0]
        print(f"My name is: {self.name}")

    def walk(self, x=0, y=0):
        self.position[0] = self.position[0] + x
        self.position[1] = self.position[1] + y

        print(f"New position: {self.position}")

    def eat(self):
        print("I am hungry")


class Dog_Robot(Robot):
    def make_noise(self):
        print("Wolf Wolf")

    def eat(self):
        super().eat()  # access the properties from the parent class
        print("I like chicken leg piece")


class Cat_Robot(Robot):
    def make_noise(self):
        print("Meow Meow")

    def eat(self):
        super().eat()
        print("I like Milk")


def main():
    my_dog = Dog_Robot("Buddy")
    my_dog.eat()

    my_cat = Cat_Robot("Tommy")
    my_cat.walk(12, 5)
    my_cat.eat()


main()
