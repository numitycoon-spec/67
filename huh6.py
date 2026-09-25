power = int(input()) #if input 50
key = input() #if input GOLD

if power >= 50:
    if key == "gold":
        print("treasure")
    else:
        print("need key")
        
else:
    print("locked")       

    