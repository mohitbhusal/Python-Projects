#from tkinter import *
import tkinter


class Application(Frame):

    def __init__(self,master):
        super(Application,self).__init__(master)
        self.master = master
        self.task = ""
        self.UserIn = tkinter.StringVar()
        self.grid() #grid creates the data into geometry physically visible in the GUI based system
        self.create_widgets()

    def create_widgets(self):
        self.user_input = tkinter.Entry(self, bg ='white', bd = 29, insertwidth = 4 , width = 24 ,
        font = ('Verdana',20,'bold'), textvariable = self.UserIn, justify = tkinter.RIGHT)
        self.user_input.grid(columnspan = 4)

        self.user_input.insert(0,'0')

        self.button1 = tkinter.Button(self, bg='green', bd = 12,
        text = "6", padx = 33 , pady = 25, font = ("Helvetica", 20, "bold"),
        command = lambda : self.buttonClick(6))
        self.button1.grid(row = 2, column = 0, sticky = W)

        self.button2 = tkinter.Button(self, bg='green', bd=12,
        text="7", padx=35, pady=25, font=("Helvetica", 20, "bold"),
        command=lambda: self.buttonClick(7))
        self.button2.grid(row=2, column=1, sticky=W)

        self.button3 = tkinter.Button(self, bg='green', bd=12,
        text="8", padx=33, pady=25, font=("Helvetica", 20, "bold"),
        command=lambda: self.buttonClick(8))
        self.button3.grid(row=2, column=2, sticky=W)

        self.button4 = tkinter.Button(self, bg='green', bd=12,
        text="9", padx=33, pady=25, font=("Helvetica", 20, "bold"),
        command=lambda: self.buttonClick(9))
        self.button4.grid(row=2, column=3, sticky=W)

        self.button4 = tkinter.Button(self, bg='green', bd=12,
        text="2", padx=35, pady=25, font=("Helvetica", 20, "bold"),
        command=lambda: self.buttonClick(2))
        self.button4.grid(row=3, column=0, sticky=W)

        self.button5 = tkinter.Button(self, bg='green', bd=12,
        text="3", padx=33, pady=25, font=("Helvetica", 20, "bold"),
        command=lambda: self.buttonClick(3))
        self.button5.grid(row=3, column=1, sticky=W)

        self.button6 = tkinter.Button(self, bg='green', bd=12,
        text="4", padx=33, pady=25, font=("Helvetica", 20, "bold"),
        command=lambda: self.buttonClick(4))
        self.button6.grid(row=3, column=2, sticky=W)

        self.button7 = tkinter.Button(self, bg='green', bd=12,
        text="5", padx=33, pady=25, font=("Helvetica", 20, "bold"),
        command=lambda: self.buttonClick(5))
        self.button7.grid(row=3, column=3, sticky=W)

        self.button8 = tkinter.Button(self, bg='green', bd=12,
        text="1", padx=35, pady=25, font=("Helvetica", 20, "bold"),
        command=lambda: self.buttonClick(1))
        self.button8.grid(row=4, column=0, sticky=W)

        self.button9 = tkinter.Button(self, bg='green', bd=12,
        text="0", padx=33, pady=25, font=("Helvetica", 20, "bold"),
        command=lambda: self.buttonClick(0))
        self.button9.grid(row=4, column=1, sticky=W)






        self.Addbutton = Button(self, bg='green', bd=12,
        text="+", padx=33, pady=25, font=("Helvetica", 20, "bold"),
        command=lambda: self.buttonClick('+'))
        self.Addbutton.grid(row=4, column=2, sticky=W)

        self.Subbutton = tkinter.Button(self, bg='green', bd=12,
        text="-", padx=33, pady=25, font=("Helvetica", 20, "bold"),
        command=lambda: self.buttonClick('-'))
        self.Subbutton.grid(row=4, column=3, sticky=W)

        self.Multbutton = tkinter.Button(self, bg='green', bd=12,
        text="x", padx=35, pady=25, font=("Helvetica", 20, "bold"),
        command=lambda: self.buttonClick('*'))
        self.Multbutton.grid(row=5, column=0, sticky=W)

        self.Divbutton = tkinter.Button(self, bg='green', bd=12,
        text="/", padx=33, pady=25, font=("Helvetica", 20, "bold"),
        command=lambda: self.buttonClick('/'))
        self.Divbutton.grid(row=5, column=1, sticky=W)

        self.Equalbutton = tkinter.Button(self, bg='green', bd=12,
        text="=", padx=33, pady=25, font=("Helvetica", 20, "bold"),
        command=self.CalculateTask)
        self.Equalbutton.grid(row=5, column=2, sticky=W)

        self.Clearbutton = tkinter.Button(self, bg='green', bd=12,
        text="AC", padx=33, pady=25, font=("Helvetica", 20, "bold"),
        command=self.ClearDisplay)
        self.Clearbutton.grid(row=5, column=3, sticky=W)

        self.Backspace = tkinter.Button(self, bg='green', bd=12,
                                  text="BS", padx=33, pady=25, font=("Helvetica", 20, "bold"),
                                  command=self.BackSpace)
        self.Backspace.grid(row=5, column=4, sticky=W)




    def buttonClick(self, number):
        self.task = str(self.task) + str(number)
        self.UserIn.set(self.task)

    def CalculateTask(self):
        self.data = self.user_input.get()
        try:
            self.answer = eval(self.data)
            self.displayText(self.answer)
            self.task = self.answer

        except SyntaxError as e:
            self.displayText("Invalid Syntax")
            self.task = ""
    def displayText(self,value):
        self.user_input.delete(0,END)
        self.user_input.insert(0,value)

    def ClearDisplay(self):
        self.task = ""
        self.user_input.delete(0, END)
        self.user_input.insert(0, '0')

    def BackSpace(self):
        self.task = ""
        self.user_input.delete(1,END)

calculator = Tk()
calculator.title("Calculator")
app = Application(calculator)

calculator.resizable(width = False, height = False)
calculator.mainloop()









