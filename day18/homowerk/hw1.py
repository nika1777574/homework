num = int(input("შეიყვანეთ რიცხვი: "))

product = 1

for i in range(1, num + 1):
    product *= i

print("ფაქტორიალია:", product)





# a % b  →  ნაშთი, რომელიც დარჩება a-ის b-ზე გაყოფის შემდეგ


num = int(input("შეიყვანეთ რიცხვი: "))


if num % 2 == 0:
    print("ეს რიცხვი ლუწია")
else:
    print("ეს რიცხვი კენტია")




num = int(input("შეიყვანეთ რიცხვი: "))

print("რიცხვის გამყოფებია:")

for i in range(1, num + 1):
    if num % i == 0:   # თუ ნაშთი 0-ია, ე.ი. i არის num-ის გამყოფი
        print(i)
   
