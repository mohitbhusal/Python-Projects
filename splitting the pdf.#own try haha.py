from PyPDF3 import PdfFileReader,PdfFileWriter

def splitter(path,length):
    reader = PdfFileReader(path)
    writer = PdfFileWriter()
    for m in range(length[0]-1,length[1]):
        page_length = reader.getPage(m)
        writer.addPage(page_length)
    with open(path_given+"splitted.pdf",'wb') as split:
        writer.write(split)
length_given=[]
path_given = input("Enter the path of pdf you wanna split")

starting= int(input('Enter The Starting Page Number You need'))
while starting>PdfFileReader(path_given).getNumPages():
    print('You Have Gone Out Of Page Please enter starting\n page no value'
          ' upto',PdfFileReader(path_given).getNumPages())
    starting = int(input('Enter The Starting Page Number You need'))

ending = int(input ('Enter The Ending Page Number You Need'))
if starting > ending:
    print('invalid input format.\n Please enter the starting page no.\n smaller than ending page no.')
elif ending>PdfFileReader(path_given).getNumPages():
    print('You Have Gone Out Of Page Please enter ending\n page no value upto',PdfFileReader.getNumPages())
elif starting<0:
    print('Either You Are doing a bad joke or trying \n to check me what happens if i do so right?')
else:
    print('Your File Is Created On the same folder of original file with name',path_given+"splitted.pdf")
length_given.append(starting)
length_given.append(ending)
splitter(path_given,length_given)





