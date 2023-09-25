l=[1,2,3,4,6,8,99,67,2]
print(l)
l.append(7)
l.sort()
# list1.sort(reverse=True)
print(l)


# print(l.index(4))this function will tell you 4 is on which index
print(l)
print(l.count(2))

# m=l.copy()
# m[0] = 0
# print(l)
# print(m)
l.insert(3,344)
# l.pop(6) it will takes out 6 from the list

print(l)


m= [100,200,400,500,600]
l.extend(m)
l.sort()
print(l)

k = l+m
print(k)