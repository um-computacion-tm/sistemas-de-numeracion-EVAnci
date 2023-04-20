def decimal_to_something(decimal, base):
    something = ''
    while decimal >= base:
        temp = decimal%base
        if temp > 9:
            temp = {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}.get(int(temp))
            print('si')
        something += str(temp)
        decimal = decimal//base
    something += str(decimal%base) + str(decimal//base)
    something = something[::-1]
    return something
xd = True
while xd:
    base = int(input('Base: '))
    print(decimal_to_something(int(input('Numero Decimal: ')), base ))
    if input('Press Enter to continue') != '':
        xd = False
