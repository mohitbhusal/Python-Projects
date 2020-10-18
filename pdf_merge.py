#Good try yet your brain is too small .mohit haha.
from PyPDF3 import PdfFileReader,PdfFileWriter

def merge(paths):
    pdf_writer = PdfFileWriter()

    for path in paths:
        pdf_reader = PdfFileReader(path)

        for pages in range(pdf_reader.getNumPages()):
            page_pages = pdf_reader.getPage(pages)
            pdf_writer.addPage(page_pages)
    with open(r"C:\Users\mohit\Desktop\merged.pdf",'wb') as merged:
         pdf_writer.write(merged)
Path = [r"C:\Users\mohit\Desktop\tensorpy.pdf",r"C:\Users\mohit\Desktop\tensorpy.pdf"]
merge(Path)
