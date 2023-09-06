def factorial(number):
    #BASE CASE
    if number == 1:
        return 1
    else:
        return number * factorial(number - 1)

print(factorial(5))