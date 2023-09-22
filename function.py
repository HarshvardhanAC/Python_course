# def addition(a,b):
#     sum = a+b
#     print(sum)
    
# a= 9
# b=10
# c=11
# d=13

# addition(a,b)
# addition(c,d)
# below example is of required arguments
def averageofafunction(a,b):
    print("The average of a two number is :-",(a+b)/2)
    
averageofafunction(6,7)

# example of default arguments
def function(a=8,b=6):
    print("The average of a two number is :-",int((a+b)/2))
    
function()