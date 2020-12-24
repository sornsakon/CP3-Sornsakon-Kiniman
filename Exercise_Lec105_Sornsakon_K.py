class Vehicle:
    lecenseCode = ""
    serialCode = ""
    name =""
    def turnOnAirConditioner(self):
        print(self.name,": Turn On Air")
class Car(Vehicle):
    name = "Car"

class Pickup(Vehicle):
    name = "PickUp"

class Van(Vehicle):
    name = "Van"

class Estatecar(Vehicle):
    name = "EstateCar"

car1 = Car()
car1.turnOnAirConditioner()

pickup1 = Pickup()
pickup1.turnOnAirConditioner()

van1 = Van()
van1.turnOnAirConditioner()

estateCar1 = Estatecar()
estateCar1.turnOnAirConditioner()