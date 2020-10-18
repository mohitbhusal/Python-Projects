def boot(a):
    ''' this is the document string '''
    def hey():
        return a().upper()
    return hey()
def state():
    return "apple is doctor"
print(boot(state))

