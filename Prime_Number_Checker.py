# Prime Number Checker function

def prime_checker(number):
    if number % 1 == number and number % number == 1:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)