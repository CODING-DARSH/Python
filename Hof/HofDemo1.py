def pdfHandler():
    print(f"pdf handler is called...")
def imageHandler():
    print(f"Image handler is called...")   
def docHandler():
    print(f"doc handler is called...")
def fileHandler(fh):
    print("File handler is called")
    fh()

fileName="abc.jpg"

if fileName.endswith(".jpg"):
    fileHandler(imageHandler)
elif fileName.endswith(".pdf"):
    fileHandler(pdfHandler)
elif fileName.endswith(".doc"):
    fileName(docHandler)
# fh=dochandler address and then fh() will call that address
