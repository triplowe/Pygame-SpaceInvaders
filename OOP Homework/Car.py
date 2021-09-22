import CarClass as c

car = c.Car(2000, "Ford")

car.accelerate()
car.accelerate()
car.accelerate()
car.accelerate()
car.accelerate()

print(car.get_speed())

car.brake()
car.brake()
car.brake()
car.brake()
car.brake()

print(car.get_speed())



