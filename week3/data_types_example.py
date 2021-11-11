
## lists = collections of the items of the same type 

a = [100, 1, 2, 3]

## tuple = collections of the items which do not have to be of the same type 
a = (100, 1, 2, 3)

b = ("Pavel", 1234)

print(f"Name is {b[0]} and student id is {b[1]}")

## dictionaries = collections of items which can be accessed by a key (a set of key - value pairs)

a = {"Pavel": 1234, "Vitaly": 1235}

print(a["Pavel"])
print(a["Vitaly"])

a["Bob"] = 9999

print(a["Bob"])

for name, id in a.items():
    print(f"{name}'s student is {id}")
    
for name in a:
    print(name)
    print(a[name])
    
if "Bob" in a:
    print(a["Bob"])
    
if "Alice" in a:
    print(a["Alice"])
