tup = (1,2,3,4,5,6,7,"green")#tuples are unchangable.How?
# tup [0] = 9 exampleand explanation how tuple is not changable
print(tup) 
print(tup[2])
print(len(tup))

if 3456 in tup:
    print("Yess")
else:
    print("no")
    
tup2 = tup[1:4]
print(tup2)