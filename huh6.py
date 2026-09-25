power = int(input())
key = input()

if power >= 50:
    if key == "gold":
        print("teasure")
    else:
        print("need key")
        
else:
    print("locked")       

    