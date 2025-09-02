data={"name":"darsh","age":18}
with open(data["name"]+".txt","a") as file:
    for i,j in data.items():
        file.write(f"{i}-->{j}\n")