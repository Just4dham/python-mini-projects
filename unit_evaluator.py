print("----------------------CONVERTER-------------------------------- ")

num = float(input("Number: "))
unit = input("Unit? ").strip().lower()

if unit.endswith(("kg", "kilogram", "kilograms")):
    target = input("grams or pounds? ").strip().lower()
    if target.startswith("gram"):  
        print(num * 1000)
    elif target.startswith(("pound", "lp")):
        print(num * 2.20462)

elif unit.endswith(("grams", "g", "gram")):
    target = input("kilograms or pounds? ").strip().lower()
    if target.startswith("kilogram"):
        print(num / 1000)
    elif target.startswith(("pound", "lp")):
        print(num * 0.00220462)

elif unit.endswith(("pounds", "lp", "pound")):
    target = input("kilograms or grams? ").strip().lower()
    if target.startswith(("kilogram", "kg")):
        print(num / 2.20462)
    elif target.startswith(("gram", "g")):
        print(num * 453.592)

elif unit.endswith(("kilometers", "km", "kilometer")):
    target = input("meter, cm or feet? ").strip().lower()
    if target.startswith(("centimeter", "centimeters", "cm")):
        print(num * 100000)
    elif target.startswith(("meter", "meters", "m")):
        print(num * 1000)
    elif target.startswith(("feet", "foot", "ft")):
        print(num * 3280.84)    

elif unit.endswith(("centimeters", "cm", "centimeter")):
    target = input("meter, kilometer or feet? ").strip().lower()
    if target.startswith(("kilometer", "kilometers", "km")):
        print(num / 100000)
    elif target.startswith(("meter", "meters", "m")):
        print(num / 100)
    elif target.startswith(("feet", "foot", "ft")):
        print(num / 30.48)    

elif unit.endswith(("feet", "ft", "foot")):
    target = input("meter, kilometer or cm? ").strip().lower()
    if target.startswith(("kilometer", "kilometers", "km")):
        print(num / 3280.84)
    elif target.startswith(("meter", "meters", "m")):
        print(num / 3.281)
    elif target.startswith(("centimeter", "centimeters", "cm")):
        print(num * 30.48)