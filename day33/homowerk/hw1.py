
numbers = [1, 2, 3]
numbers.append(4)  

numbers.insert(1, 10)  

numbers.pop()



my_list = [10, 20, 30, 40, 50]


print(len(my_list))




numbers = []

for i in range(5):
    num = int(input("შეიყვანეთ რიცხვი: "))
    numbers.append(num)  
print(numbers)



colors = ["red", "green", "blue", "yellow", "purple"]

colors.pop()  

print(colors)


animals = ["dog", "cat", "elephant", "lion"]


animals.insert(1, "monkey")

print(animals)



students = []


for i in range(3):
    name = input("შეიყვანეთ სტუდენტის სახელი: ")
    students.append(name)


students.insert(0, "Teacher")

students.pop()


print("სიის სიგრძე:", len(students))

print("საბოლოო სია:", students)


def sum_numbers(a, b):
    return a + b


def check_even(number):
    if number % 2 == 0:
        print("რიცხვი ლუწია")
    else:
        print("რიცხვი კენტია")


def square(number):
    return number ** 2


def full_name(name, surname):
    print(f"ჩემი სახელია {name} და გვარია {surname}")

