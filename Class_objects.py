class person :
    name = "Harry"
    occupation = "Software developer "
    income = "100000"
    
    def info():
        print(f"The emolyee name is {self.name} and he is a {self.occupation} with income of {self.income} ")
    
a= person()
b=person()


a.name = "shubham"
a.occupation = "Accountant"
a.income = "15000"


b.name = "Harish"
b.occupation = "Teacher"
b.income = "20000"


b.info()