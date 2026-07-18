from pypdf import PdfReader #Imports the tool that knows how to read PDF files.
from docx import Document #Imports the tool that knows how to read Word documents.


def extract_resume_text(file): #Creates a machine that takes a resume file and produces text.

    filename = file.filename.lower() #Gets the file name and converts it to lowercase for consistency.

    if filename.endswith(".pdf"): #Checks if the uploaded file is a PDF.

        reader = PdfReader(file) #Creates the PDF expert.

        text = "" #Creates an empty box to store all resume text.

        for page in reader.pages: #If the PDF has 3 pages, Python loops 3 times.

            text += page.extract_text() #Adds the text from the current page to the box.

        return text

    elif filename.endswith(".docx"): #Checks if the uploaded file is a Word document.

        document = Document(file) #Creates the Word-document expert.

        text = "" #Creates an empty box to store all résumé text.

        for paragraph in document.paragraphs: #Loops through every paragraph in the Word document.

            text += paragraph.text + "\n" #Adds the current paragraph and a line break to the final text.

        return text
    
    else:

        return ""