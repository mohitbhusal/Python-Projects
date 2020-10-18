#program which rotes the specific page of a pdf
from PyPDF3 import PdfFileReader, PdfFileWriter

def rotate(pdf_path):
    pdf_reader=PdfFileReader(pdf_path)
    pdf_writer=PdfFileWriter()#writer path is ot declared but is declared at last after making the pdf and assigining th

    page_1=pdf_reader.getPage(0).rotateClockwise(90)
    pdf_writer.addPage(page_1)
    for pages in range(1,pdf_reader.getNumPages()):
        page_pages = pdf_reader.getPage(pages)
        pdf_writer.addPage(page_pages)
    with open(r"C:\Users\mohit\Desktop\rotated_page.pdf",'wb') as any:
        pdf_writer.write(any)


if __name__=='__main__':
    path = r"C:\Users\mohit\Desktop\tensorpy.pdf"
    rotate(path)


