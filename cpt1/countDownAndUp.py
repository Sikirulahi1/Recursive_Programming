def countDownAndUp(number):
    print(number)
    if number == 0:
        # BASE CASE
        print('Returning from base case')
        return
    else:
        #RECURSIVE CASE
        countDownAndUp(number - 1)
        print(f"{number} returning")
        return

countDownAndUp(3)