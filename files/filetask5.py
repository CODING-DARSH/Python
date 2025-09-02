def copy_file():
    with open("th.txt","r") as file1:
        with open("newwfile.txt","w") as file2:
            for i in file1.readlines():
                file2.writelines(i)
copy_file()
print("File copied successfully")