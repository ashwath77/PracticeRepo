#

def factorial_num(num):
    fact = 1
    for i in range(1,num+1):
        fact=fact*i
    return fact

print(factorial_num(5))
