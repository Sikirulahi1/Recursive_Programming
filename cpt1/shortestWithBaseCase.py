def shortestWithBaseCase(makeRecursiveCall):
    print(f"Shortest with base case called. ({makeRecursiveCall})")
    if not makeRecursiveCall:
        # Base Case
        print('Returning from base case.')
        return
    else:
        # Recursive Case
        shortestWithBaseCase(False)
        print('Returning from recursive case.')
        return


print('Calling shortest with base case:')
shortestWithBaseCase(False)
print()
shortestWithBaseCase(True)