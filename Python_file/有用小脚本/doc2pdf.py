import os
from win32com import client

def doc2pdf(doc_name,pdf_name):
    """
    word转化为pdf
    :param doc_name:
    :param pdf_name:
    :return:
    """
    try:
        word=client.DispatchEx('Word.Application')
        if os.path.exists(pdf_name):
            os.remove(pdf_name)
        worddoc=word.Documents.Open(doc_name,ReadOnly=1)
        worddoc.SaveAs(pdf_name,FileFormat=17)
        worddoc.Close()
        return pdf_name
    except:
        return 1
if __name__=='__main__':
    docname=input('please enter docname')
    pdfname=input('please enter pdfname')
    doc2pdf(docname,pdfname)