# Converting an iterative algorithm to a recursive one
# Write hello,World five times.

print('Code in a loop:')
i = 0
while i < 5:
 print(i, 'Hello, world!')
 i = i + 1


print('Code in a recursion:')
def hello(i = 0):
    print(f"{i}, Hello, world!")
    i += 1
    
    if i < 5:
       
        hello(i)
    

hello()