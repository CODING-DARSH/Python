def pdfHandler(fileName):
    print(f"pdf handler is called...{fileName}")
def imageHandler(fileName):
    print(f"Image handler is called...{fileName}")   
def docHandler(fileName):
    print(f"doc handler is called...")
def fileHandler(fh,fileName):
    print("File handler is called")
    fh(fileName)
fileName="abc.jpg"

if fileName.endswith(".jpg"):
    fileHandler(imageHandler,fileName)
elif fileName.endswith(".pdf"):
    fileHandler(pdfHandler,fileName)
elif fileName.endswith(".doc"):
    fileHandler(docHandler,fileName)