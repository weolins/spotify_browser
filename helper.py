import webbrowser

def timer(ms):
    seconds = ms // 1000
    minutes = seconds // 60
    seconds = seconds % 60
    
    formatted_time = f"{minutes:02}:{seconds:02}"
    
    return formatted_time

def asker(urlss, type):
    print("\nDo you want to play any of these songs?\nY.Yes\nN.Go Back")
    console = input("> ")
    
    while console != 'N':
        if console == "Y":
            player(urlss,type)
            return
        else:
            print ("Invalid Input. Try Again.")
        print("\nDo you want to play any of these songs?\nY.Yes\nN.Go Back")
        console = input("> ")
    
    return


def player(urlss, type):
    
    if type == 'S':
        slist = ["1","2","3","4","5"]
        msg = "1-5"
    else: 
        slist = ["1","2","3","4","5","6","7","8","9","10"]
        msg = "1-10"

    print(f"\nWhich song do you want to play?({msg}) Enter E to exit.")
    console = input("> ")
        
    while console != 'E':
        if console in slist:
            webbrowser.open(urlss[int(console)-1])
            return
        else:
            print ("Invalid Input. Try Again.")
        print("\nWhich song do you want to play?(1-5) Enter E to exit.")
        console = input("> ")
    
    return