set1={1,2,3,4,5}
set2={3,4,5,6,7}
# Union = set1.union(set2)
# print(Union)

# # with union update the set 
# set1.update(set2)

# set3=set1.intersection(set2)
# print(set3)
set3=set1.symmetric_difference(set2)#excluding the comman part
print(set3)
