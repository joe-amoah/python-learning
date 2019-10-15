# A python program that create a number guessing game

m = (1,99)
guess = int(raw_input("Enter an integer from 1,99:"))
while m < guess:
    print
    if guess < m:
        print "guess is down"
        guess = int(raw_input("Enter an integer from 1,99: "))
    elif guess > m:
        print "guess is up"
        guess = int(raw_input("Enter an integer from 1,99:"))
    else:
        print "you guessed it"
        break
        print
