"""

A dictionary is a collection which is ordered, changeable and do not allow duplicates.


"""
dict1 = {"name":"musthahsina","age":"25","place":"abc","course":"python"}
print(dict1)
print(dict1["name"])
print(dict1.get("name"))
dict1.update({"course":"React:"})
print(dict1)
x=dict1.keys()
print(x)
y=dict1.values()
print(y)
print(dict1.popitem())
print(dict1)
d=dict1.keys()
print(d)

x = ('key1', 'key2', 'key3')
y = 0,1,2,3

thisdict = dict.fromkeys(x, y)

print(thisdict)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("model", "bronco")

print(x)

print("name" in dict1)

