class vehicle:
    def __init__(self,wheels):
        self.wheels = wheels
    def display(self):
        print(f"Wheels: {self.wheels}\t",end='')

class harley(vehicle):
    def __init__(self, wheels,model,speed):
        super().__init__(wheels)
        self.model = model
        self.speed = speed

    def display(self):
        super().display()
        print(f"Model: {self.model}\tSpeed: {self.speed} kmph")

street_bob = harley(2,"Milwaukee-Eight 114", 180)

street_bob.display()
street_bob.display(2023)