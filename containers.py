# A Python program tha compute and displaying the refund and returning containers.
less = 0.10
more = 0.25
less_cans = input("How many less containers did you recycle?")
more_cans = input("How many more containers did you recycle?")
less_cansPrices = less * int(less_cans)
more_cansPrice = more * int(more_cans)
totalRefund = int(less_cans) + int(more_cans)
print("The total refund of the bottles is $" + str(totalRefund) + ".")
