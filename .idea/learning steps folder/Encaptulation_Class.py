class car:
    def __init__(self,speed,colour):
        self.__speed = speed
        self.__colour = colour

    def set_speed(self,value):
        self.__speed = value

    def get_speed(self):
        return self.__speed
ford = car(250,'violet')
ford.set_speed(400)
ford.set_speed(500)
ford.colour = 'purple'
# print(ford.speed)
# print(ford.get_speed())
# print(ford.colour)