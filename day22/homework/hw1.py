# 1-დან 5-მდე რიცხვების დაბეჭდვა
for i in range(1, 6):
    print(i)




# 1-დან 5-მდე რიცხვების დაბეჭდვა
i = 1
while i <= 5:
    print(i)
    i += 1



num = int(input("შეიყვანე რიცხვი: "))

if num > 0:
    print("დადებითი რიცხვია")
elif num < 0:
    print("უარყოფითი რიცხვია")
else:
    print("ნულია")



for i in range(1, 11):
    if i % 2 == 0:
        print(i, "ლუწია")
    else:
        print(i, "კენტია")




for i in range(1, 11):
    if i % 2 == 0:
        if i > 5:
            print(i, "ლუწი და 5-ზე მეტია")
        else:
            print(i, "ლუწი და 5-ზე ნაკლებია")
    else:
        print(i, "კენტია")
