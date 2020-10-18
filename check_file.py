
m = ""
class data:

    def __init__(self,value):
        self.value = value+','
        self.start_list = []
        self.end_list = []
        self.single_data = []
        global m
        for contains in self.value:
            m = m + contains
            if ',' in m:
                if '-' in m:
                    starter = m[:m.index('-')]
                    ender = m[m.index('-')+1:m.index(',')]
                    self.start_list.append(starter)
                    self.end_list.append(ender)
                    m = ''
                elif not '-' in m :
                    single_page = m[:m.index(',')]
                    self.single_data.append(single_page)
                    m=''

    def start(self):
        return self.start_list

    def end(self):
       return self.end_list

    def single(self):
        return self.single_data



# a = '1,2,5,6-7,8-9,4-5,8,2-5'
# print(data(a).single())
# print(data(a).start())
# print(data(a).end())
# start =data(a).start()
# end = data(a).end()
