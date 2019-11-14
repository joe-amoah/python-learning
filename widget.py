# A Python program that  reads the number of Widgets and the number of Gizmos in an order from the user.
numOfWidgets = input("Enter the number of widget:")
numOfGizmos = input("Enter the number of Gizmos:")
converts1 = int(numOfWidgets)
converts2 = int(numOfGizmos)

weightOfWidgets = converts1 * 75
weightOfGizmos = converts2 * 112
totalWeight = weightOfWidgets + weightOfGizmos
convert3 = str(totalWeight)
print("")
print("The total weight of the weight is" + convert3)

