# Factorial using recursive
def fact_rec(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fact_rec(n-1)
    
number = int(input("Enter The Number : "))
res=fact_rec(number)
print(f"The Factorial of {number} is {res}")