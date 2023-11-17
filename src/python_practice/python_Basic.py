# 1. Write a program to perform input/output of all basic data types. including (sets, dict, list, tuple and strings)
a=7
b=7.77
c=1+1j
d={"Animal:lion","Car:BMW"}
e=a>b
s={1,2,3,4,5,6,7,8}
l=[1,2,3,4,5,6,78,9,9]
t=(1,2,3,4,5,6,7,8,7)
st="Ashwath gowda"
z={}
print(type(a),type(b),type(c),type(d),type(e),type(s),type(l),type(t),type(st),type(z))

#2. Write a program to find power of any number x ^ y.
x=int(input("Enter the base value: "))
y=int(input("Enter the expo value: "))
print("Power value is: ",x**y)

#3. Write a program to enter any number and calculate its square root.
x=int(input("Enter the squareroot value: "))
z=x**(1/2)
print("square root: ",z)

#4. Write a program to enter two angles of a triangle and find the third angle.
a=int(input("Enter the 1st angle: "))
b=int(input("Enter the 2nd angle: "))
c=180-a-b
print("last angle: ",c)

#5. Write a program to enter base and height of a triangle and find its area.
base=int(input("Enter the base of the triangle: "))
height=int(input("Enter the height of the triangle: "))
area=(1/2)*base*height
print("Area of Triangle: ",area)

#6. Write a program to enter marks of five subjects and calculate total, average and percentage
p=int(input("Enter 1st subject marks: "))
c=int(input("Enter 2nd subject marks: "))
m=int(input("Enter 3rd subject marks: "))
b=int(input("Enter 4th subject marks: "))
k=int(input("Enter 5th subject marks: "))
total=p+c+m+b+k
avearage=total/5
#average=(p+c+m+b+k)/5
percentage=(total/500)*100
print("Total:Average:Percentage = ",total,avearage,percentage)

#7. Write a program to enter P, T, R and calculate Simple Interest.P=principle amount,T=Time,R=Rate of I
P=int(input("Enter the principal amount: "))
T=int(input("Enter the time periods in year: "))
R=int(input("Enter the rate of interest per annum: "))
Simple_Interest = (P*T*R)/100
Amount=P+Simple_Interest
print("Simple Interest:Total_Amount ",Simple_Interest,Amount)

#8. Write a program to find maximum between two numbers
a=int(input("Enter the value1: "))
b=int(input("Enter the value2: "))
if a>b:
    print("A is greater: ",a)
else:
    print("B is greater: ",b)

#9. Write a program to find maximum between three numbers.
a=int(input("Enter the value1: "))
b=int(input("Enter the value2: "))
c=int(input("Enter the Value3: "))
if a>b and a>c:
    print("A is greater",a)
elif b>a and b>c:
    print("B is greater",b)
elif c>a and c>b:
    print("C is greater",c)
else:
    print("Some numbers are identical cannot compare to give greater please check the values")

#10. Write a program to check whether a number is divisible by 5 and 11 or not.
num=int(input("Enter the number to input: "))
if num%5==0 and num%11==0:
    print("Number is divisible")
else:
    print("Number is not divisible")

#11. Write a program to check whether a number is even or odd.
num=int(input("Enter the number to input: "))
if num%2==0:
    print("Even num: ",num)
else:
    print("Odd num: ",num)


#12. Write a program to check whether a year is leap year or not.
year=int(input("Enter the year: "))
if (year%4==0 and year%400==0 and year%100==0 ) or (year%4==0 and year%100!=0):
    print("Leap year")
else:
    print("Not a leap year")

#13. Write a program to print numbers from 1 to 10.:
i=1
while i<=10:
    print(i,end=" ")
    i+=1

#14. Write a program that prompts the user to input a positive integer. It should then print the
# multiplication table of that number.
user=int(input("Input a positive integer: "))
i=1
while i<=10:
    z=user*i
    i+=1
    print(user,"*",i-1,"=",z)

# 15. Write a program to calculate the sum of following series where n is
# input by user.
# 1 + 1/2 + 1/3 + 1/4 + 1/5 +…………1/n
n=int(input("Enter the input: "))
sum=0
for i in range(1,n+1):
    sum+=1/i
    print("Sum of the following series: ",sum)
