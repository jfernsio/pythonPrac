from PyPDF2 import PdfFileWriter, PdfFileReader
writer = pdfFileWriter()
file = 'test_file.pdf'
reader = PdfFileReader(file)
for page in range(reader.numPages):
    writer.addPage(reader.getPage(page))
writer.encrypt('Password') 
with open(f'test_file.pdf', 'wb') as file:
    writer.write(file)
print(('PDF encrypted'))       