class hospital():

    '''this is the file made to create
    the employees details of MCROSS hospital'''
    def __init__(self,deg,**proff):
        self.deg = deg
        self.proff = proff
    # def change_proff(self,**nxt):
    #     self.proff = nxt
    def printing(self):
        return (self.proff,self.deg)
list= {'Milan':'ENT','Hari':'cardiologist'}
print(hospital('MBBS',list))



