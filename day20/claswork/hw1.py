
total = 0  

for i in range(5):
    num = int(input("შეიყვანეთ რიცხვი: "))
    total += num

print("ჯამი არის:", total)

if total % 2 == 0:
    print(total, "- ეს რიცხვი ლუწია")
else:
    print(total, "- ეს რიცხვი კენტია")
 


while True:
    num = int(input("შეიყვანეთ რიცხვი: "))

    if num % 5 == 0 and num % 7 == 0:
        print("სწორია! რიცხვი:", num)
        break   
    else:
        print("ეს რიცხვი არ არის 5-ის და 7-ის ჯერადი, სცადეთ თავიდან.")





balance = int(input("შეიყვანეთ თქვენი ბალანსი: "))

if balance >= 1500:
    print("თქვენ შეგიძლიათ იყიდოთ: ლეპტოპი")
elif balance >= 1000:
    print("თქვენ შეგიძლიათ იყიდოთ: ტელეფონი")
elif balance >= 100:
    print("თქვენ შეგიძლიათ იყიდოთ: ფეხსაცმელი")
elif balance >= 50:
    print("თქვენ შეგიძლიათ იყიდოთ: პერანგი")
elif balance >= 5:
    print("თქვენ შეგიძლიათ იყიდოთ: რვეული")
else:
    print("სამწუხაროდ, ამ ბალანსით ვერ ყიდულობთ ჩამოთვლილ ნივთებს.")



num = int(input("შეიყვანეთ რიცხვი: "))

if num > 0:
    print("ეს რიცხვი დადებითია.")
elif num < 0:
    print("ეს რიცხვი უარყოფითია.")
else:
    print("ეს რიცხვი არის ნული.")





