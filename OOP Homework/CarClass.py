class Car:

    def __init__(self, yearModel, make):
        self.__yearModel = yearModel
        self.__make = make
        self.__speed = 0

    def set_yearModel(self, yearModel):
        self.__yearModel = yearModel
    
    def set_make(self, make):
        self.__make = make
    
    def set_speed(self, speed):
        self.__speed = speed
    
    def get_yearModel(self):
        return self.__yearModel

    def get_make(self):
        return self.__make
    
    def get_speed(self):
        return self.__speed
    
    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5

    