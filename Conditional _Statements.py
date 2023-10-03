# print(True)
# print(type(True))

# print(False)
# print(type(False))

# Question on compariosn operator
# p,q,r = eval(input("Enter the Number :-"))
# print("The value of p,q,r is:-",p,q,r)

# print("(p>q>r)",p>q>r)
# print("(p<q<r)",p<q<r)
# print("p<q and q<r",p<q and q<r)
# print("p>r and q>r",p>r and q>r)

# if-statement

# question two compare the values of operand
# a= eval(input("Enter the value of a:-"))
# b= eval(input("Enter the value of b:-"))
# if(a==b):
#     print("Both the values are equal means a==b",a==b)



# printing the area and circumferance of the circle taking radius input
# radius=eval(input("Enter the radius :- "))
# print("The radius of circle is :-",radius)
# if radius>0 :
#     pi=22.7
#     area = pi*radius*radius
#     print("The area of c2ircle is",(area))
    
#     cicumferance= 2*pi*radius
#     print("The circumferance of a circle is :-",cicumferance)
    
# if-else
# Greater number
# a=eval(input("Enter the number :-"))
# b=eval(input("Enter the number :-"))

# print("The value of a is :-",a)
# print("The value of b is :-",b)

# if(a>b):
#     print("a is greater than b")
# else:
#     print("b is greater than a")
    

# # Question on sales and salary
# Sales=float(input("Enter the Total amount of Sales done in Month :-"))
# print("The Monthly sales goes upto :-","Rs:-", Sales)

# if Sales>=100000 :
#     Basic = 4000
#     HRA = 20 * Basic/100
#     DA = 110 * Basic/100
#     conveyance = 500
#     Incentive = Sales * 10/100
#     bonus = 1000
# else:
#     Basic = 4000
#     HRA = 10 * Basic/100
#     DA = 110 * Basic/100
#     conveyance = 500
#     Incentive = Sales * 4/100
#     bonus = 500
    
# salary = (Basic+HRA+DA+conveyance+Incentive+bonus)
# print(f"The total salary of Employee after the Monthly sales of{Sales} is :-",salary)


# Divisibilty Test

# number = input("Enter the Number:-")
# Number= int(number)
# print("The Number is :-",Number)
# if Number%5 ==0 and Number%10 ==0 :
#     print(f"The {Number} is Divisible by 5 and 10")
# else :
#     print("You have entered the Wrong number")
    
# print("The Number is :-",Number)
# if Number%5 ==0 or Number%10 ==0 :
#     print(f"The {Number} is Divisible by 5 or 10")
# else :
#     print("You have entered the Wrong number")

# Nested if-else
# Greatestof 3

Num1 = eval(input("Enter the number :-"))
Num2 = eval(input("Enter the number :-"))
Num3 = eval(input("Enter the number :-"))

print("The following number entered are :-",Num1,Num2,Num3)

if Num1 > Num2 :
    if Num1 > Num3 :
        print("The Num1 is greater")
    else:
        print("The Num3 is greater")
elif  Num2 > Num1:
    if Num2 > Num3:
        print("The Num2 is greater")
    else:
        print("The Num3 is greater")
else:
    print("The Num3 is greater by Default")