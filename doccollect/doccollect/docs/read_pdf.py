from io import StringIO
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.layout import LAParams
from pdfminer.converter import TextConverter
from pdfminer.pdfpage import PDFPage

def extract_text(filename):
    with StringIO() as output, open(filename, 'rb') as f:
        parser = PDFParser(f)
        doc = PDFDocument(parser)
        manager = PDFResourceManager()
        converter = TextConverter(manager, output, laparams=LAParams())
        interpreter = PDFPageInterpreter(manager, converter)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)
        return output.getvalue()
