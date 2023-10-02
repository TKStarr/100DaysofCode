n=int(input("Please enter a number between 1 and 100."))

def prime_checker(number = n):
    if number > 100 or number < 1:
        print("That number is not between 1 and 100.")
    else:
        is_prime = True
        for i in range (2, number):
            if number % i == 0:
                is_prime = False
        if is_prime == True:
            print("It's a prime number.")
        else:
            print("It's not a prime number.")

prime_checker(n)