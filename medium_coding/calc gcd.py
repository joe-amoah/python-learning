# Program that calculate GCD

def gcd(a,b):
    if a == 0:
        return a
    else:
        return gcd(b,a % b)
