# upper()
# ყველა ასოს აქცევს დიდ ასოდ (uppercase)

text = "hello world"
print(text.upper())      

print("python".upper())  

name = "Nika"
print(name.upper())      


# lower()
# ყველა ასოს აქცევს პატარა ასოდ (lowercase)

text = "HELLO WORLD"
print(text.lower())     

print("PyThOn".lower())  

email = "USER@MAIL.COM"
print(email.lower())     



# .capitalize()
# მხოლოდ პირველი ასო ხდება დიდი, დანარჩენი — პატარა

text = "hello world"
print(text.capitalize())   

print("pYTHON".capitalize())  

sentence = "gEORGIA"
print(sentence.capitalize())  
 


# .title()
# ყოველი სიტყვის პირველი ასო ხდება დიდი

text = "hello world"
print(text.title())     

print("python programming language".title())

name = "nika gvaramia"
print(name.title())      



# .find()
# აბრუნებს სიმბოლოს/ტექსტის პირველ ინდექსს
# თუ ვერ იპოვა — აბრუნებს -1-ს

text = "hello world"
print(text.find("h"))    

print(text.find("world"))  

print(text.find("x"))    
