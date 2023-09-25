try:
    number=input("Enter the number :-")
    print(f"The entered number is {number}")

    if number > 0 :
        print("Yo are good to go ahead")
        
    else:
        print("entered the value less than 0")

except:
    print("Value Error")  
    
finally :
    print("Conclusion :- Always Enter the Correct value")  
 