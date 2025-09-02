with open("th.txt", "r") as file:
    longest_length = 0
    longest_line = ""
    
    for i in file.readlines():
        count = 0
        for ch in i:
            if ch != "\n":      
                count += 1
        if count > longest_length   : 
            longest_length = count
            longest_line = i     

print("Length of longest line:", longest_length)
print("Longest line:", longest_line)
