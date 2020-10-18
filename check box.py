
from tkinter import *
from tkinter import filedialog
root = Tk()

def browsefunc():
    filename = filedialog.askopenfilename()
    pathlabel.config(text=filename)
    return(filename)

def text_out():
    printer =  Entry(bg ='white', bd = 29, insertwidth = 7 , width = 29 ,
        font = ('Verdana',20,'bold'), textvariable = StringVar(), justify = RIGHT)
    lebeler.config(text=printer)
lebeler = Label(root)
lebeler.pack()
pathlabel = Label(root)
pathlabel.pack()
browsebutton = Button(root, text="Browse", command=browsefunc)
browsebutton.pack()

saver = browsefunc()
#print(saver)

from PyPDF3 import PdfFileReader,PdfFileWriter
import check_file

def splitter(path,start_pg,end_pg,single_pg):
    reader = PdfFileReader(path)
    writer = PdfFileWriter()
    for l in range((len(start_pg))):
        for m in range(int(start_pg[l])-1,int(end_pg[l])):
            page_length = reader.getPage(m)
            writer.addPage(page_length)
    for each in single_pg:
        get_page = reader.getPage(int(each)-1)
        writer.addPage(get_page)
    with open(saver+"splitted.pdf",'wb') as split:
        writer.write(split)

#path_given = input("Enter the path of pdf you wanna split")

page=input('Enter The Page Number You need')
pg =check_file.data(page)
starting= pg.start()
ending = pg.end()
single = pg.single()
# for st in starting:
#     while int(st)>PdfFileReader(path_given).getNumPages():
#         print('You Have Gone Out Of Page Please enter starting\n page no value'
#             ' upto',PdfFileReader(path_given).getNumPages())
#         page = input('Reenter The Page Number You need')
#
# for st in range(len(starting)-1):
#
#         if int(starting[st]) > int(ending[st]):
#             print('invalid input format.\n Please enter the starting page no.\n smaller than ending page no.')
#             page = input('Reenter The Page Number You need')
#         elif int(ending[st])>PdfFileReader(path_given).getNumPages():
#             print('You Have Gone Out Of Page Please enter ending\n page no value upto',PdfFileReader.getNumPages())
#             page = input('Reenter The Page Number You need')
#         elif int(starting[st])<0:
#             print('Either You Are doing a bad joke or trying \n to check me what happens if i do so right?')
#             page = input('Reenter The Page Number You need')
#         else:
#             print('Your File Is Created On the same folder of original file with name',path_given+"splitted.pdf")
# for each in single:
#      if int(each)>PdfFileReader(path_given).getNumPages():
#          print('You Have Gone Out Of Page Please enter ending\n page no value upto', PdfFileReader.getNumPages())

splitter(browsefunc(),starting,ending,single)
print(starting)
print(ending)

