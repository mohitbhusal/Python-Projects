from PyPDF3 import PdfFileReader

def nikalpdf(pdf_path):
    with open(pdf_path,'rb') as t:
        pdf = PdfFileReader(t)
        info = pdf.getDocumentInfo()
        no_of_pg = pdf.getNumPages()

    text = f"""
    Information about{pdf_path}
    Author: {info.author}
    Creator: {info.creator}
    Producer: {info.producer}
    Subject: {info.subject}
    Title: {info.title}
    Number of Pages: {no_of_pg}
    read: {pdf}"""

    print(text)
    return info
if __name__=='__main__':
    path=r'C:\Users\mohit\Desktop\tensor4.pdf'
    nikalpdf(path)
