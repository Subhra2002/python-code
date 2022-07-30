
# what is factorial Value😎🤞🤷‍♂️
# factorial of 4 = 1*2*3*4

# n = 4
# product=1
# for i in range(n):
#     product = product * (i+1)

# print(product)


def factorial_itret(n):
    product = 1
    for i in range(n):
        product= product*(i+1)
    return product

print(factorial_itret(5))

def factorial_recursive(n):
    if n == 1 or n==0:
        return 1
    return n * factorial_recursive(n-1)
    
print(factorial_recursive(1))