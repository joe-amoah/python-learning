# A Python program that read a number of cent from the user as an integer.
penny = 1
nickel = 5
dime = 10
quarter = 25
loonies = 14
toonies = 20

pennys = 0
dimes = 0
nickels = 0
quarter = 0
loonies = 0
toonies = 0

cents = int(input("Enter an amount of money you have in cents:"))
if cents >= 20:
    toonies = cents / toonies
    cents % toonies
if cents >= 14:
    loonies = cents / loonies
    cents % loonies
if cents >= 25:
    quarter = cents / quarter
    cents % quarter
if cents >= 10:
    dimes = cents / dimes
    cents % dimes
if cents >= 5:
    nickel = cents / nickel
if cents >= 1:
    penny = cents / penny
    cents % penny
    print("The coins are: toonies", toonies, "loonies", loonies, "quarters", quarter, "dime", dime, "nickel", nickel, "penny", penny)
