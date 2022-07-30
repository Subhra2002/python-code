# Find the greatest number between three numbers 😉🐱‍🏍

def maximum(num1, num2, num3):
    if num1 > num2:
        if num1 > num3:
            print(f"{num1} is the highest number among three")
        else:
            print(f"{num3} is the highest number among three")
    else:
        if num2 > num3:
            print(f"{num2} is the highest number among three")
        else:
            print(f"{num3} is the highest number among three")

n1 = int(input("Enter the 1st number: "))
n2 = int(input("Enter the 2nd number: "))
n3 = int(input("Enter the 3rd number: "))
s = maximum(n1,n2,n3)
print(s)
