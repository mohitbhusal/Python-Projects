# from learn3 import *
#
#
# class child(parent):
#     def __init__(self, attr, attr2, atter3):
#         super(child, self).__init__(attr, attr2, atter3)
#         self.child_behave()
#
#     def child_behave(self):
#         a = parent('cat', 'apple','cat')
#         return(a)
#
# child('apple','ball','cat').child_behave()

from tkinter import *
from tkinter import filedialog
root = Tk()

def browsefunc():
    filename = filedialog.askopenfilename()
    #pathlabel.config(text=filename)
    return(filename)
pathlabel = Label(root)
pathlabel.pack()
browsebutton = Button(root, text="Browse", command=browsefunc)
browsebutton.pack()
#print(browsefunc())



#mainloop()
