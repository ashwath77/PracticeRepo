#1.Please enter your name to receive a welcome message from the program?
def wellcomeall():
    name=input("Enter the name: ")
    return "Hello" +" "+name

# 2.Find the factorial of a input positive number.
def factorial_num(num):
    fact = 1
    for i in range(1,num+1):
        fact=fact*i
    return fact

#3. Write a program that prompts the user to input a positive integer. It should then print the
# multiplication table of that number.

def multiplication_num(num):
    mul=1
    for i in range(1,11):
        mp_num = num*i
        print("num",num,"*",i,"=",mp_num)

# 4. Two numbers are entered through the keyboard. Write a program to find the value of one
# number raised to the power of another. (Do not use built-in method)

def exponential_number(num1,num2):
    expo=1
    for i in range(1,num2+1):
        expo=num1*expo
    return num1,"**",num2,"=",expo

#5. Write a program that prompts the user to input an integer and then
# outputs the number with the digits reversed. For example, if the input
# is 12345, the output should be 54321.

def reversing_number(num):
    rev=0
    while num>0:
        digit=num%10
        rev=rev*10 + digit
        num=num//10
    return "Reversed: ",rev

# 6. Write a program that reads a set of integers, and then prints the sum
# of the even and odd integers.

def sum_of_even_odd_numbers(num):
    even_num=0
    odd_num =0
    for i in range(1,num+1):
        if i%2==0:
            even_num+=i
        else:
            odd_num+=i
    print("Sum of even numbers: ",even_num)
    print("Sum of odd numbers: ", odd_num)

# 7. Write a program that prompts the user to input a positive integer. It
# should then output a message indicating whether the number is a
# prime number.

def prime_numbers(num):
    flag =True
    for i in range(2,num):
        if num%i==0:
            flag=False
            print("Not prime",num)
            break
    else:
        print("prime number: ",num)


#8. Write a program to calculate HCF of Two given number.
def Highest_Common_Factor(num1,num2):
    hcf=1
    for i in range(1,num1+1 or num2+1):
        if num1%i==0 and num2%i==0:
            hcf=i
    print("Highest common factor is : ",hcf)

#9. Write a program to calculate LCF of Two given number.
def Least_Common_Multiple(num1,num2):
    hcf=1
    for i in range(1,num1+1 or num2+1):
        if num1%i==0 and num2%i==0:
            hcf=i
    lcm=hcf*(num1//hcf)*(num2//hcf)
    print("least common multiple is : ",lcm)


# 10. Write a program to print Fibonacci series of n terms where n is input
# by user : 0 1 1 2 3 5 8 13 21 34 .....

def Fibonacci_series(num):
    a=0
    b=1
    for i in range(num):
        print("Fibonacci numbers:",a,end=" ")
        a,b = b,a+b













