#Default პარამეტრი არის ფუნქციის პარამეტრი, რომელსაც წინასწარ აქვს მინიჭებული მნიშვნელობა


def my_function(name="nika"):
    for i in range(len(name)):
        print(name[i])
my_function()
my_function("Giorgi")