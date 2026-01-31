
names = ["Nika", "Ana", "Giorgi", "Mariam", "Luka"]

user_name = input("შეიყვანეთ სახელი: ")
names.append(user_name)

print("append-ის შემდეგ სია:", names)

names.insert(3, "Tarieli")
print("insert-ის შემდეგ სია:", names)

names.pop(4)
print("pop-ის შემდეგ სია:", names)

names.remove("Ana") 
print("remove-ის შემდეგ სია:", names)

search_name = input("შეიყვანეთ სახელი მოსაძებნად: ")

if search_name in names:
    print("სახელის index არის:", names.index(search_name))
else:
    print("not index in list")