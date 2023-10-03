# While loop is conditioned controlled loop executes whenever the condition gets true and executes the block of code inside and comes out of the loop whenever the condition gets false
# Printing values usung while loop

# count = 0
# while count <=5 :
#     print('Count =',count)
#     count=count+1

# num =1 
# sum=0
# while num <=10 :
#     print("Num =",num)
#     sum = sum+num
#     num=num+1
# print("The sum of numbers are",sum)



# # For Loop
# # Question1 :- Printing Number 1 to 5
# for i in range(1,6):
#     print("The Following numbers are :-")
#     print(i)


# # Question2 
# for i in range(65,91,1):
#     print(chr(i),end=",")

# Question3 
#print number from  1 to 10 in reverse order

# for i in range(10,0,-1):
#     print("i =",i) 
    
# Question 4
# print  square of first five number 

# for i in range(1,6,1):
#     Square= i*i
#     print("Square of a Number is :-",Square)
    
    
# print("loop Ends")

# sum = 0
# for i in range (1,11,1):
#     if i%2==0 :
#         print("i=",i)
#         sum= sum + i
        
        
# print("The sum of above number is :-",sum)

# Question5
# Sum of number 1 to 20  which is not divisible 2,3 and 5
# sum = 0
# for i in range(1,20,1):
#     if i%2 == 0 or i%3 == 0 or i%5 == 0 :
#         print("")
#     else:
#         print(i)
#         sum=sum+i 
        
# print("The Sum is :-",sum)

# Multiplication table 
# for i in range(1,6):
#     for j in range(1,11):
#         Multiplication= i*j
#         print(f"The Multiplication of {i} * {j} = ",Multiplication)
#     print("\n") 

# for i in range(6,0,-1):
#     for j in range (1,i,1):
#         print( " * ",end=" ")
        
#     print()
    
# k=2
# for  i in range (5,0,-1):
#    for j in range (1,k,):
#        print("*",end="")
#        k=k+1
#    print()
   


# for i in range(1,7,1):
    # for j in range(1,i,1): here 1 is decreasing in loop so it is printing 0  the on 2 it is printing 1so lower one is more correct
#         print(j,end="")
        
#     print() 
    
# for i in range(1,6,1):
#     i=i+1
#     for j in range(1,i,1):
#         print(j,end="")
        
#     print() 

for i in range(5,0,-1):
    i=i+1
    for j in range(1,i,1):
        print(j,end="")
        
    print() 
        
        
        