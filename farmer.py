# A python program that reads the length and width of a farmer field from the user in feet.
# and then display the area of the field in acres

length = float(input("Enter the length of the field in feet"))
width = float(input("Enter the width of the field in feet"))
acres = length * width / 43560
print("The area of the field is", acres, "acres")
