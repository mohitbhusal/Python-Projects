class car():
    def __init__(self,speed,colour):
        self.speed = speed
        self.colour = colour

    def set_speed(self,value):
        self.speed = value

    def get_speed(self):
        return self.speed
ford = car(250,'violet')
ford.set_speed(500)
ford.colour = 'purple'
