def a():
    spam = 'Ant'
    print(f'spam is {spam}')
    b()
    print(f'spam is {spam}')

def b():
    spam = 'Bobcat'
    print(f'spam is {spam}')
    c()
    print(f'spam is {spam}')
    
def c():
    spam = 'Cocyte'
    print(f'spam is {spam}')

a()