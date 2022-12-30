import os
import PyPDF2
from io import BytesIO
from docx import Document



class ConvertToWord:
    def __init__(self):
        # Open the PDF file in read-binary mode
        ///class to convert the pdf class to word//
        with open('input.pdf', 'rb') as file:
            # Create a PDF object
            self.pdf = PyPDF2.PdfFileReader(file)

        self.text = []

        # Iterate through each page of the PDF
        for page in range(self.pdf.getNumPages()):
            # Extract the text from the page
            page_text = self.pdf.getPage(page).extractText()
            # Append the text to the list
            self.text.append(page_text)

        # Create a new Word document
        document = Document()

        # Iterate through the list of text
        for page in self.text:
            # Add a new paragraph to the Word document
            paragraph = document.add_paragraph(page)

        # Save the Word document
        document.save('output.docx')
