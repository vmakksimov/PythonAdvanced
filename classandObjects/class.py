class Person:
    def __init__(self, name):
        self.name = name
        self.age = 27

    def say_hi(self):
        print(f'Hi, my name is {self.name}')

    def fuck_you(self):
        print(f'I wanna fuck you {self.age}')

jordan = Person('Viktor Maksimov')
jordan.say_hi()
jordan.fuck_you()