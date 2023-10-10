class proffesion :
    
    def __init__(self,name,occupation) :
        self.name = name
        self.occupation = occupation
        
    def info(self) :
            print(f'Your name is {self.name} your work profession is {self.occupation}')
            
a= proffesion("Harsh","Learner")

a.info()
class addition :
    
    def __init__(self,a,b) :
        
        self.a = a
        self.b = b
        
    def add(self,a,b):
      print(f"the sum of {self.a} and {self.b} is =",(a+b))
      
c= addition(5,6)
c.add(5,6)