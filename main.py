class GearBoxType:
    name: str
    remarks: str


class GearBox:
    gearRatio: float
    currentGear: int

    def shiftUp(self):
        pass

    def shiftDown(self):
        pass


class Tire:
    width: float
    airPressure: float


class Wheel:
    diameter: float


class Suspention:
    springRate: float


class Brake:
    type: str

    def apply(self):
        pass


class CarModel:
    title: str


class Car:
    registrationNum: str
    year: int
    licenseNum: str

    def moveForward(self):
        pass

    def moveBackward(self):
        pass

    def stop(self):
        pass

    def tumRight(self):
        pass

    def tumLeft(self):
        pass


class Engine:
    capacity: float
    numberOfCylinders: int

    def start(self):
        pass

    def brake(self):
        pass

    def accerate(self):
        pass


class Body:
    numberOfDoors: int


car_model = CarModel()
gear_box_type = GearBoxType()
gear_box = GearBox()
gear_box.type = gear_box_type

tire = Tire()
wheel = Wheel()
wheel.tire = tire

suspension = Suspention()
brake = Brake()
suspension.wheel = wheel
brake.wheel = wheel

engine = Engine()
body = Body()

car = Car()
car.car_model = car_model
car.gear_box = gear_box
car.suspension = suspension
car.brake = brake
car.body = body
car.engine = engine
print(car.year)
# переробити, всі поля зробити нормальними