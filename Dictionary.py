# dic= {
#     "Harry" : "Human being",
#     "Spoon" : "Object"
#     }

# print(dic["Harry"])

info = {
    "Name":"Harsh",
    "Age":22,
    "Sex":"Male",
    "Occupation":"Still learning",
    "Hope":"Postive"
    }
print(info)
print(info["Occupation"])
print(info.get("Age"))
print(info.values())
print(info.keys())
for i in info.keys():
    print(f"The keys for the above statement are {info[i]}")
    