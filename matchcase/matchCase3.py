choice = input(f"please enter y,yes,Y for enter in game and \nn,no,N for exit and  \nm,menu,M for menu: ")

match choice:
    case 'y' | 'Y' | 'yes':
        print("welcome to game:")
    case 'n' | 'N' | 'no':
        print("thanks for coming..")    
    case 'm' | 'menu' | 'M':
        print("menu options....")    
    case _:
        print("invalid choice...")
        