#########################
#   Little description  #
#########################

# Wrapper functions can be very useful for improving code organization,
# reducing code duplication, and enhancing the functionality and usability 
# of existing functions.
# In this case, this wrapper function solve all the convertions, but recieves
# 2 parameters. So the real convertion functions call this wrapper function 
# specifying the correct base, and giving the number recieved.

# How this wrapper function works?
# It recieves 2 parameters, the number to convert and the base.
# Then it goes to a while loop, it adds at the firts the remainder in a variable 
# called convertion till the number divided is lower than the base. There is a
# final line that add the final result of the last divition to the convertion
# There are some if's to change numbers to characters in case of hexadecimal.

#########################
#    Wrapper function   #
#########################

def decimal_wrapper(decimal, base):
    convertion = ''
    while decimal >= base:
        resto = decimal % base
        if resto > 9:
            resto = {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}.get(resto)
        decimal = decimal // base
        convertion = str(resto) + convertion
    if decimal > 9:
        decimal = {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}.get(decimal)
    convertion = str(decimal) + convertion
    return convertion

#########################
#   RequestedFunctions  #
#########################

def decimal_to_binary(decimal):
    return decimal_wrapper(decimal, 2)

def decimal_to_octal(decimal):
    return decimal_wrapper(decimal, 8)

def decimal_to_hexadecimal(decimal):
    return decimal_wrapper(decimal,16)