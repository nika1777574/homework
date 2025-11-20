# loop (ციკლი) — ეს არის კონსტრუქცია, რომელიც ერთსა და იმავე მოქმედებას
# ბევრჯერ ასრულებს ავტომატურად


# range() — ეს არის ფუნქცია, რომელიც ქმნის რიცხვების მიმდევრობას
# 1) range(stop)
# 2) range(start, stop)
# 3) range(start, stop, step)




for i in range(100, 201):
    print(i)



for i in range(20, 31, 3):
    print(i)


for i in range(0, 21, 2):
    print(i)


 


nika = 0  # აქ შევინახავთ ჯამს

for i in range(5):  # 5-ჯერ ვასრულებთ შემოტანის პროცესს
    num = int(input("შეიყვანეთ რიცხვი: "))
    nika += num  # შემოტანილი რიცხვი ემატება ჯამს

velo= nika / 5  # ვიღებთ საშუალოს
print("საშუალო არითმეტიკული არის:", velo)



