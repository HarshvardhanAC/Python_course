class person :
    # name = "Harry"
    # occupation = "Software Developer"
    # Networth = 10
    
    def info (self):
        print(f"{self.name} is a {self.occupation} ")
    
    
a = person()
a.name = 'Harshvardhan'
a.occupation = "Billioner"
# a.Networth = "World Richest Person" 
# print(a.name,a.Networth,a.occupation)
a.info()