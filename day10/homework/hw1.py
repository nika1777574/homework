# ==  →  ტოლია
a = 5 == 5      # True
b = 10 == 7     # False
c = "hi" == "hi"  # True
d = 3.0 == 3    # True
e = [1,2] == [1,2]  # True

# !=  →  არ არის ტოლი 
a = 5 != 7      # True
b = 10 != 10    # False
c = "dog" != "cat"  # True
d = 3.5 != 3.6  # True
e = [1,2] != [2,1]  # True

# >  →  მეტია
a = 10 > 5      # True
b = 7 > 9       # False
c = 3.5 > 3.0   # True
d = -1 > -5     # True
e = 100 > 100   # False

# <  →  ნაკლებია
a = 3 < 7       # True
b = 10 < 5      # False
c = -2 < 0      # True
d = 4 < 4       # False
e = 2.5 < 3.5   # True

# >=  →  მეტია ან ტოლი
a = 5 >= 5      # True
b = 10 >= 3     # True
c = 4 >= 7      # False
d = -1 >= -1    # True
e = 8 >= 2      # True

# <=  →  ნაკლებია ან ტოლი
a = 4 <= 4      # True
b = 2 <= 5      # True
c = 9 <= 1      # False
d = 0 <= 3      # True
e = -2 <= -2    # True










# Python-ში არსებობს სამი მთავარი ლოგიკური ოპერატორი:
# 1) and
# 2) or
# 3) not

# 1) and  →  აბრუნებს True-ს მხოლოდ მაშინ, როცა ორივე პირობა ჭეშმარიტია


x = (5 > 2) and (10 > 3)   # True and True → True
y = (5 > 2) and (10 < 3)   # True and False → False
z = (1 == 1) and (2 == 2)  # True and True → True
k = (4 < 2) and (3 < 5)    # False and True → False
m = (10 > 9) and (5 == 5)  # True and True → True

# 2) or  →  აბრუნებს True-ს მაშინ, როცა მინიმუმ ერთი პირობა მაინც ჭეშმარიტია


x = (5 > 2) or (10 > 3)    # True or True → True
y = (5 > 2) or (10 < 3)    # True or False → True
z = (1 == 2) or (2 == 2)   # False or True → True
k = (4 < 2) or (3 < 1)     # False or False → False
m = (10 > 9) or (5 != 5)   # True or False → True

# 3) not  →  აბრუნებს პირობის საპირისპირო მნიშვნელობას (ინვერსიას აკეთებს)

x = not (5 > 2)     # not True → False
y = not (10 < 3)    # not False → True
z = not (1 == 1)    # not True → False
k = not (4 != 4)    # not False → True
m = not (3 < 5)     # not True → False





number = int(input("შეიყვანეთ ნებისმიერი რიცხვი: "))


fixed_number = 10


number > fixed_number
print("შეყვანილი რიცხვი მეტია 10-ზე.")
number == fixed_number
print("შეყვანილი რიცხვი ტოლია 10-ის.")

print("შეყვანილი რიცხვი ნაკლებია 10-ზე.")






name = input("შეიყვანეთ თქვენი სახელი: ")


my_name = "Nika"


name == my_name
print()

print("სახელი არ ემთხვევა")













age = int(input("შეიყვანეთ თქვენი ასაკი: "))


age > 18
print("თქვენ სრულწლოვანი ხართ")
age == 18
print("თქვენ ზუსტად 18 წლის ხართ")

print("თქვენ არასრულწლოვანი ხარ.")

9