# Merging PDFs

The following code combines PDFs in a directory into one file. 

Here we are using `glob`, but you can also just list out the PDF names like: 

`pdfs = ['pdf1.pdf', 'pdf2.pdf']`

```python
from PyPDF2 import PdfFileMerger
import glob

pdfs = glob.glob('*.pdf')

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("to_print.pdf")
merger.close()