from tkinter import *


class Application(Frame):

    def __init__(self, master): # Why is 'master' called?
        super(Application, self).__init__(master)    # ?
        self.grid()
        self.create_widgets()
        # self.flash()

    def create_widgets(self):
        self.bttn1 = Button(self, text = "This is a button").grid()
        # self.bttn1.grid()

root = Tk()
root.title("Lazy Buttons 2")
root.geometry("200x85")
app = Application(root)
root.mainloop()