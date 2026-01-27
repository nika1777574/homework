
text = "Hello World Hello Python"

print(text.upper())

print(text.lower())

print(text.capitalize())

print(text.title())

index_o = text.find("o")
print(index_o)

second_o = text.find("o", index_o + 1)
print(second_o)

not_found = text.find("z")
print(not_found)

substring_index = text.find("World")
print(substring_index)
