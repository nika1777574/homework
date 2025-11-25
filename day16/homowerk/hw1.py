
for i in range(10, -11, -1):
    print(i)



for i in range(1, 101, 2):
    print(i)





correct_password = "goa123"
attempts = 3  # სულ 3 მცდელობა

while attempts > 0:
    password = input("Enter password: ")

    if password == correct_password:
        print("Access granted!")
    
    else:
        attempts -= 1
        print("Password is incorrect! Try again.")
    
        if attempts > 0:
            print("You have", attempts, "attempts left.")
        else:
            print("No attempts left! Access denied.")
