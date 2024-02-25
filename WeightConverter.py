weight = int(input("Enter weight :"))
unit = input("Unit (L)kbs or (K)g :")

if unit.upper() == "L":
    convert = weight * 0.45
    print(f"Your weight is {round(convert, 2)} kilos")
elif unit.upper() == "K":
    convert = weight / 0.45
    print(f"Your weight is {round(convert, 2)} pounds")
else:
    print("Invalid input")