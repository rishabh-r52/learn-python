map = {
    "name":"Rishabh",
    "usn":67,
    "age":23,
    "edu":{
        "x": "DAV",
        "xii": "SCL",
        "college": "VKIT"
    }
}

print(map)
print(map["age"])

# del map["usn"]
values = map.pop("usn")

print(values)

print(map)

for key,value in map.items():
    print(key,value)

print(map["edu"]["x"])



marks = {
    "semester":"fifth", 
    "english":88, 
    "chemistry":91
    }

print(marks)

marks["computer"] = 75

print(marks)

marks["chemistry"] = 67

print(marks)

print(marks["english"])
print(marks["semester"])




my_dict = {
    'Alice': {
        'age': 25,
        'location': 'New York'
    },
    'Bob': {
        'age': 30,
        'location': 'San Francisco'
    }
}

print(my_dict["Alice"]["age"])




dict = {"delhi":25_000_000, "mumbai":20_000_000, "bangalore":13_000_000, "new york":40_000_000}

max_pop = 0
max_key = ""

for key in dict:
    if max_pop < dict[key]:
        max_pop = dict[key]
        max_key = key

print(max_key,dict[max_key])

str = "abc"
str2 = "def"
s2 = str.join(str2)
print(s2)