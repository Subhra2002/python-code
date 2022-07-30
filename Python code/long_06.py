def recursive_natural(n):
        if n == 1:
            return 1
        else:
            if n== 0:
                return 0
            else:
                return recursive_natural(n-1) + n
                
n = int(input("Enter the natural number"))   
s = recursive_natural(n)
print(s)

