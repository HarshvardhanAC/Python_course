a= input("Enter the number:")
print(f"The Multiplication values of {a} is :-")

try :
 for i in range(1,11):
    print(f"The answer is {a} X {i} = {int(a)* i}")
except:
    print("The Invalid value has been entered")
    
print("Due to the exception handling the rest program will run fine if any exception occur")

try :
    num = int(input("Please Enter the Number :"))
    a= [ 6,3]
    print(a[num])
except ValueError:
    Print("Number Entered is not a integer.")
    
except IndexError:
  print("Index Error")  
        