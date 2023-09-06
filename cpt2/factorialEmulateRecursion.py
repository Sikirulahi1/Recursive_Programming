# Understanding how we can the iterative loop can be used to write thr recursion function.
# Hard to code out.

callStack = [] # The explicit call stack, which holds "frame objects". 1
callStack.append({'returnAddr': 'start', 'number': 5}) # "Call" the "factorial() function". 2
returnValue = None


while len(callStack) > 0:
    # The body of the "factorial() function":
    number = callStack[-1]['number'] # Set number parameter.
    returnAddr = callStack[-1]['returnAddr']
    if returnAddr == 'start':
        if number == 1:
            
            # BASE CASE
            returnValue = 1
            callStack.pop() # "Return" from "function call". 3
            continue
        else:
            
            # RECURSIVE CASE
            callStack[-1]['returnAddr'] = 'after recursive call'
            
            # "Call" the "factorial() function":
            callStack.append({'returnAddr': 'start', 'number': number - 1})
        continue
    
    elif returnAddr == 'after recursive call':
        returnValue = number * returnValue
        callStack.pop() # "Return from function call". 5
        continue
print(returnValue)