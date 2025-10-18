from PyPDF2 import PdfReader, PdfWriter


pdf_password = "aababsbasasa"
r = PdfReader(r"C:\Users\rajsn\Downloads\CPC_IO.pdf")
if r.is_encrypted:
    r.decrypt(pdf_password)

w = PdfWriter()
for p in r.pages:
    w.add_page(p)
with open("CPC_IO_unlocked.pdf", "wb") as f:
    w.write(f)
