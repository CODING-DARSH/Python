# file=open("wfile1.txt","w")
# file.write("My name is darsh")
# file.close()
# file=open("wfile2.txt","a")
# file.write("My name is darsh \nI am studying in blr\n I am studying aiml branch")
# file.close
with open("files\myfile1.txt","a") as file:
    file.writelines("I am darsh vithlani")
    print("Data successfully entered in file")