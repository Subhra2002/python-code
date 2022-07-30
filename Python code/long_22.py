while(True):
    print("Enter q for quit this game")
    a = (input("Enter a Number Greater then 0 :"))
    if a =='q':
        print("You press q to quit")
        break

    try:
        a = int(a)
        if a>0:
          print(f"Your Number is greater then 0 and Your number is {a}")
    except Exception as e:
        print(e)
print("Thanks for playing this Game ! Please come next time ")