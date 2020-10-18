# class parent(object):
#     def __init__(self, attr, attr2, atter3):
#         self.attr = attr
#         self.attr2 = attr2
#         self.atter3 = atter3
#
#     def method1(self):
#         return (self.attr)
#
#     def method2(self):
#         return (self.attr2)
#
#     def method3(self):
#         return (self.atter3)

import tkinter as tk


r = tk.Tk()


l = tk.Label(text = 'press f to make button flash')
l.pack()

b = tk.Button(text = 'useless button', command = l.config(text = filedialog.askopenfilename()))
b.configure(bg = 'purple',activebackground = 'red')
b.pack()

# def flash(event):
#     b.configure(bg = 'yellow')
#     r.after(200, lambda: b.config(bg = 'lightgrey'))
#
# r.bind('<Button-1>',flash)

r.mainloop()