thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

thisdict["year"] = 2018

for x, y in thisdict.items():
  print(x, y)

print(len(thisdict))

thisdict["color"] = "red"

del thisdict["model"]
