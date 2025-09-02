choice = input(f"please enter y for enter in game and \nn for exit and  \nm for menu: ")

match choice:
    case 'y':
        print("welcome to game:")
    case 'n':
        print("thanks for coming..")    
    case 'm':
        print("menu options....")    
    case _:
        print("invalid choice...")
        