class Animal:
    def __init__(self):
        self.number_eyes = 2

    def breath(self):
        print("Inhale, Exhale")

class Fish(Animal):

    def __init__(self):
        super().__init__()

    def breath(self):
        super().breath()
        print("doing this under water")

    def swim(self):
        print("moving in the water")

nemo = Fish()
nemo.swim()
nemo.breath()
print(nemo.number_eyes)