
cars = ["BMW", "Audi", "Mercedes", "Toyota", "Honda",
    
     "Ford", "Nissan", "Kia", "Hyundai", "Volkswagen"]

print("მე-5 ელემენტი:", cars[4])

new_list = cars[1:6]
print("ახალი სია:", new_list)
print("ახალი სიის ბოლო ელემენტი:", new_list[-1])

print("ყოველი მეორე ელემენტი:", cars[::2])

print("მე-3-დან მე-8-მდე ყოველი მესამე:", cars[3:9:3])

first_five = cars[:5]
reversed_list = first_five[::-1]
print("შემოტრიალებული სია:", reversed_list)

copied_cars = cars
copied_cars[7] = "Tesla"

print("ორიგინალი სია:", cars)
print("დაკოპირებული სია:", copied_cars)


numbers = [3, 7, 12, 5, 9]

for num in numbers:
    print(num)

