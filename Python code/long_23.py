try:
    a = int(input("Enter a number : "))
    c = 1/a
    print(c)

except ValueError as e:
    print("Please Enter a valid number")
    print(e)

except ZeroDivisionError as e:
    print("Make sure that you does not enter 0")

print("Thanks for using the Game ")