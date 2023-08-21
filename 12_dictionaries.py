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