print("######################## WELOCME TO PS5 #############################")
choice = int(input(f"Press 1 for fortnit \nPress 2 for FIFA \nPress 3 for GTA\n"))

match choice:
    case 1:
        print("WELCOME TO FORNIT")
        mode = input("press s for single player \n press d for dual player")
        match mode:
            case 's':
                print("Game satrts playing as single player")
            case 'd':
                print("Game satrts playing as dual player")
            case _:
                print("invalid choice start again...")    
    
    case 2:
        print("WELCOME TO FIFA")
        mode = input("press s for single player \n press d for dual player")
        match mode:
            case 's':
                print("Game satrts playing as single player")
            case 'd':
                print("Game satrts playing as dual player")
            case _:
                print("invalid choice start again...")            