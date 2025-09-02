def pdfHandler():
    print(f"pdf handler function called...")
    

def docHandler():
    print(f"doc handler function called...")

def imageHandler():
    print(f"image handler function called...")
        

#cb -- call back..
def fileHandler(cb):
    print("file handler called...")
    #cb == any of above function
    cb() #pdf..doc..image...

#fileHandler(pdfHandler())     ()
#fileHandler(pdfHandler)

fileName = "abc.pdf"
if fileName.endswith(".jpg"):
    fileHandler(imageHandler)
elif fileName.endswith(".pdf"):
    fileHandler(pdfHandler)
elif fileName.endswith(".doc"):
    fileHandler(docHandler)    
