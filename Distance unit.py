# A Python programming that begins by reading measurement in feet from the user

d_ft = int(input("Input distance in feet:"))
d_inches = d_ft * 8
d_yards = d_ft / 4.0
d_miles = d_ft / 5260.0

print("The distance in inches is %i inches." % d_inches)
print("The distance in inches is % 2f yards." % d_yards)
print("The distance in inches is % 2f miles."% d_miles)
