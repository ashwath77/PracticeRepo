#1. Write a Python program to sum all the items
num=int(input("Enter the number: "))
l=[]
sum=0
for i in range(1,num+1):
    l.append(i)
    sum+=i
print(l)
print("sum all the items: ",sum)

#2. Write a Python program to multiply all the items in a list
n=int(input("Enter the number: "))
l=[]
mul=1
for i in range(1,n+1):
    l.append(i)
    mul*=i
print(l)
print("mul all the items in list : ",mul)

#3. Write a Python program to get the smallest number from a list
n=int(input("Enter the numbers: "))
l=[]
for i in range(n):
    a=int(input("Enter the list iteams: "))
    l.append(a)
print(l)
largest=max(l)
smallest=min(l)
print(smallest)
print(largest)

#4. Write a Python program to clone or copy a list
l=[1,2,45,65,66]
l1=list(l)
print(l1)

#5. Write a Python program to add a list to the second list
l=[1,2,3,5]
l1=[9,8,44,66,8]
l.extend(l1)
print(l)

#6. Write a Python program to find the second smallest number in a list
l=[5,6,2,3,8,6,45,64,20,855,56]
l.sort()
print(l,'\n',"Second smallest num: ",l[1])

#7. Write a Python program to remove duplicates from a list
l=[1,"asa",1,22,75,"asa",344,1,58]
x=set(l)
print(x)


#8. Reverse the tuple
t = (1,2,3,4,5,6,7)
print(t[::-1])

#9. Access value 20 from the tuple
t = (10,20,30,40,50)
print("Value = ",t[1])

#10. Unpack the tuple into 4 variables
t =(2,4,6,8)
a,b,c,d = t
print(a)
print(b)
print(c)
print(d)

#11. Swap two tuples in Python
t1 = (1,2,3)
t2 = (4,5,6)
t1,t2 = t2,t1
print(t1)
print(t2)