class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale")


class Fish(Animal):
    def __init__(self):
        super().__init__()
        self.num_fin = 1

    def breathe(self):
        super().breathe()
        print("doing underwater")

    def swim(self):
        print("Swim in Water")


nemo = Fish()
print(nemo.num_eyes)
nemo.breathe()
nemo.swim()
dog = Animal()
dog.breathe()
print(nemo.num_fin)