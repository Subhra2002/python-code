# marks = [90,80,70,30]
# percentage = (sum(marks)/400)*100
# marks = [90,80,60,30]
# percentage2 = (sum(marks)/400)*100
# marks = [90,10,70,30]
# percentage3 = (sum(marks)/400)*100

# print(percentage , percentage2 , percentage3)

def percentagefun(totalmark):
    return (totalmark/400)*100

marks1 = int(input("Enter your 1st number : "))
marks2 = int(input("Enter your 1st number : "))
marks3 = int(input("Enter your 1st number : "))
marks4 = int(input("Enter your 1st number : "))

totalmark = marks1 + marks2 + marks3 + marks4

percentage = percentagefun(totalmark)
print(percentage)