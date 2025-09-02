name = input("Enter your name: ")
age = int(input("Enter your age: "))

with open("files/taskfile1.txt", "a") as file1:
    file1.write(f"My name is {name}\nMy age is {age}\n")
    print("File created successfully")