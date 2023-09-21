x = int(input("Enter the number")) 
print("The number is",x)


match x:
    case 0:
        printf("x is zero")
    case 4:
        printf("X is four")
        
    case _ if x!=90:
        print(x,"is not 90") 
    case _ if x!=80:
        printf(x,"is not 80")
        
        
    case _:
        print(x)   
        