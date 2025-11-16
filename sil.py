while True:

    try:
        myname = str(input("Pls enter your name: "))
        myage = str(input("Pls enter your age: "))
        print(myname, myage)
    except:
        print("Pls enter wrong input")