class car():
    ''' this is the docstring
    '''
    info="this are the cars with details"
    def __init__(self,brand='not mentioned',model='not mentioned',colour='not mentioned',type='not mentioned',milage='not mentioned',):
        self.brand=brand
        self.model=model
        self.colour=colour
        self.milage=milage
        self.type=type
    def co2_emission(self):
        return f"co2_emission = {2392/ self.milage}"

class owner(car):
    def further(self):
        return   2392/self.milage
print(owner(milage = 40).co2_emission())
print(owner(milage = 40).further())

choice = car('mitshubishi','Pajero','matt_black','suv',30)
print(choice.info)
print(choice.brand)
print(car.info)
print(choice.co2_emission())



