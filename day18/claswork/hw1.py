num = int(input("შეიყვანეთ რიცხვი: "))

if num > 50:
    print(num * 5)
else:
    print(num ** 2)



password = input("შეიყვანეთ პაროლი: ")

if password == "goa123":
    print("Password is correct!")
else:
    print("Incorrect password!")




num = int(input("შეიყვანეთ რიცხვი: "))

niik = 0

for i in range(1, num + 1):
    niik += i

print("ჯამი არის:", niik)
