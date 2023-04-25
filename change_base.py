#########################
#   Little description  #
#########################

# Wrapper functions can be very useful for improving code organization,
# reducing code duplication, and enhancing the functionality and usability 
# of existing functions.
# In this case, this wrapper function solve all the convertions, but recieves
# 2 parameters. So the real convertion functions call this wrapper function 
# specifying the correct base, and giving the number recieved.

# How decimal wrapper function works?
# It recieves 2 parameters, the number to convert and the base.
# Then it goes to a while loop, it adds at the firts the remainder in a variable 
# called convertion till the number divided is lower than the base. There is a
# final line that add the final result of the last divition to the convertion
# There are some if's to change numbers to characters in case of hexadecimal.

#########################
#   Wrapper functions   #
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

def bin_oct_hex_to_decimal_wrapper(number, base):
    number = str(number)
    num_length = len(number)
    decimal = 0
    for i in range(num_length):
        # print(f'decimal = {decimal} + ({number[i]} x 2^{num_length-1-i})')
        if number[i] in 'ABCDEF':
            block = {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}.get(number[i])
        else:
            block = int(number[i])
        decimal += block * base**(num_length-i-1)
    return decimal


###########################
##   RequestedFunctions  ##
###########################

########################
#   Decimal Base Cal   #
########################

def decimal_to_binary(decimal):
    return decimal_wrapper(decimal, 2)

def decimal_to_octal(decimal):
    return decimal_wrapper(decimal, 8)

def decimal_to_hexadecimal(decimal):
    return decimal_wrapper(decimal,16)

########################
#   Binary Base Cal    #
########################

def binary_to_decimal(binary):
    return bin_oct_hex_to_decimal_wrapper(binary, 2)

def binary_to_octal(binary):
    return decimal_to_octal(binary_to_decimal(binary))

def binary_to_hexadecimal(binary):
    return decimal_to_hexadecimal(binary_to_decimal(binary))

########################
#   Octal Base Calc    #
########################

def octal_to_decimal(octal):
    return bin_oct_hex_to_decimal_wrapper(octal, 8)

def octal_to_binary(octal):
    return decimal_to_binary(octal_to_decimal(octal))

def octal_to_hexadecimal(octal):
    return decimal_to_hexadecimal(octal_to_decimal(octal))

########################
#   Hexad Base Calc    #
########################

def hexadecimal_to_decimal(hexadecimal):
    return bin_oct_hex_to_decimal_wrapper(hexadecimal, 16)

def hexadecimal_to_binary(hexadecimal):
    return decimal_to_binary(hexadecimal_to_decimal(hexadecimal))

def hexadecimal_to_octal(hexadecimal):
    return decimal_to_octal(hexadecimal_to_decimal(hexadecimal))
