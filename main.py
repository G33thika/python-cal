nlist = []
print("If you want to exit Enter 0")
while True:
    try:
        inum = int(input("Enter value:"))
        nlist.append(inum)

        if inum != 0:
            t=0
            for x in nlist:
                t=t+x
            print(f"Curent Total = {t}")
        else:
            print(f"Total = {t}")
            break
    except KeyboardInterrupt:
        print("If you want to exit, enter 0")
        pass
    except ValueError:
        print("Invalid value \nplease enter numbers")
        pass
    except EOFError:
        print("Invalid value \nplease enter numbers")
        pass   
