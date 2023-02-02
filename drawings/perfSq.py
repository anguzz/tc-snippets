side = int(input("enter sides of square  : "))

print("Square Star Pattern") 

for x in range(side):
    for y in range(side):
        if  (x==0 and y==0) or (x==side-1 and y==0) or (y==side-1 and x==0) or (x==side-1 and y==side-1):
            print('-', end = '  ')
        else:
            print('*', end = '  ')
    print()