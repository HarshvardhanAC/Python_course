marks = [12,56,32,98,12,45,1,4]

index = 0

for mark in marks :
    print(mark)
    if (index ==3):
     print("Harry,Awesome!!\n")
    index=index+1
    
    
# withenumerate function

for index,mark in enumerate (marks):
    print("\n",mark)
    if(index ==3):
        print("Harry,awesome")