#Question1:->Take an input year from user and decide whether it is a leap year or not.
year=int(input("Enter a year to check whether the year is leap year or not "))
if(year%4==0 and year%100==0 and year%400==0):
    print("{} is a Leap year".format(year))
else:
    print("{} is not a leap year".format(year))
print()

#Question2:->Take length and breadth input from user and check whether the dimensions are of square or rectangle. 
length=int(input("Enter length of the object : "))
breadth=int(input("Enter breadth of the object : "))
if(length==breadth):
    print("Our object is of square shape")
else:
    print("Our object is of rectangle shape")
print()

#Question3:->Take the input age of 3 people and determine oldest and youngest among them.
age_1=int(input("Enter the age of first person : "))
age_2=int(input("Enter the age of Second person : "))
age_3=int(input("Enter the age of third person : "))
temp_max=max(age_1,age_2,age_3)
temp_min=min(age_1,age_2,age_3)
print("The oldest one having age {}".format(temp_max))
print("The youngest one having age {}".format(temp_min))
print()
#Question4:->Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and then using following rules print their place of service. 

#1. if employee is female, then she will work only in urban areas. 
#2. if employee is a male and age is in between 20 to 40 then he may work in anywhere 
#3. if employee is male and age is in between 40 t0 60 then he will work in urban areas only. 
#4. And any other input of age should print "ERROR". 
age=int(input("Enter the age : "))
sex=input("Enter sex male or female : ")
merital=input("Enter merital status yes or no : ")
if(sex=='female'):
    print("Employee will work only in urban area")
elif(sex=='male' and age>=20 and age<40):
    print("Employee work anywhere")
elif(sex=='male' and age>=40 and age<=60):
    print("he may work in urban areas only")
else:
    print("ERROR")
print()

#Question5:->A shop will give discount of 10% if the cost of purchased quantity is more than 1000.Ask user 
#for quantity Suppose, one unit will cost 100. 
#Judge and print total cost for user. 
quantity=int(input("Enter total units : "))
temp=quantity*100
if(temp>=1000):
    new=temp/10
    temp=temp-new
    print("Total cost of the user is :",temp)
else:
    print("User can't get any kind of discount",end='\n')
    print("Total cost of user is :",temp)
print()

#LOOPS
#Question1:->Take 10 integers from user and print it on screen.
number=int(input("Enter total number of integers : "))
list=[]
print("Enter the values : ")
for i in range (0,number):
    num=int(input())
    list.append(num)
print("The numbers are :",end=' ')
for i in range (0,len(list)):
    print(list[i],end=" ")
print()

#Question2:->Write an infinite loop.An infinite loop never ends. Condition is always true.
num1=21
while(num1>0):
    print("Infinite loop")
print()

#Question3:->Create a list of integer elements by user input. Make a new list which will store square of 
#elements of previous list.
number=int(input("Enter total number of integers : "))
list1=[]
print("Enter the values : ")
for i in range (0,number):
    num=int(input())
    list1.append(num)
list2=[]
for i in range (0,len(list1)):
    list2.append(list1[i]*list1[i])
print("The numbers are :",end=' ')
for i in range (0,len(list2)):
    print(list2[i],end=" ")
print()

#Question4:->From a list containing ints, strings and floats, make three lists to store them separately.
liist=[1,2,22.1,'hi','hello',54.3]
l_1=[]
l_2=[]
l_3=[]
for i in liist:
    if int==type(i):
        l_1.append(i)
    elif float==type(i):
        l_2.append(i)
    elif str==type(i):
        l_3.append(i)
print("Integer list : ",l_1)
print("Float list : ",l_2)
print("String list : ",l_3)
print()

#Question5:->Using range(1,101), make a list containing only prime numbers. 

num_1=1
num_2=101
li1=[]
print("Prime numbers between {} and {} are".format(num_1,num_2))
for i in range (num_1,num_2+1):
    if i>1:
        isDivisible=False
        for index in range(2,i):
            if i%index==0:
                isDivisible=True
        if not isDivisible:
            li1.append(i)
print("The new list of prime numbers is : ",li1)
print()

#Question6:-> Print the following patterns: 
'''
* 
** 
*** 
****
'''
for i in range(0,4):
    for j in range(0,i+1):
        print('*',end=' ')
    print('\n')
print()

#Question7:->Take inputs from user to make a list. Again take one input from user and search it in the list 
#and delete that element, if found. Iterate over list using for loop. 

num01=int(input("Enter number of elements"))
li01=[]
print("Enter the values : ")
for i in range(0,num01):
    new1=int(input())
    li01.append(new1)
print(li01)
del1=int(input("Enter a number which you want to delete : "))
if del1 in li01:
    li01.remove(del1)
else:
    print("Entered element does not exist in the list")
print()
























