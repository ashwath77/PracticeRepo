#1. Write a Python program to create a set
l=[1,2,3,4,5]
set_1=set(l)
print("creating a set:",set_1)

#2. Write a Python program to iteration over sets
s={1,2,3,4,5,6,7,8}
for i in s:
    print(i,end=" ")

#3. Write a Python program to add member(s) in a set
s={1,2,3,4,5,6}
s.add('s')
print(s)

#4. Write a Python program to remove item(s) from a given set
n=int(input("Enter the iteration: "))
s=set()
for i in range(n):
    a=int(input("Enter the set values: "))
    s.add(a)
print("Set of: ",s)
n=int(input("Enter the removeing set: "))
s.remove(n)
print("Removed set: ",s)

#5. Write a Python program to create a union of sets
s1 = {1,2,3,4,5}
s2 = {1,3,5,7}
print(s1.union(s2))

#6. Write a Python program to find maximum and the minimum value in a set
s1 = {1,2,3,4,5}
a= max(s1)
b= min(s1)
print("maximum value:minimum value ",a,":",b)
