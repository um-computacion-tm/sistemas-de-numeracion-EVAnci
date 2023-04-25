# Change Numeration System Base
A numeration system is a method of representing numbers using symbols, such as digits or letters, to express the quantity of objects or values. It is a systematic way of counting or expressing numbers that allows for easy understanding, communication, and computation of mathematical operations.

Numeration systems can vary in their base or radix, which is the number of digits or symbols used to represent numbers. For example, the decimal system, which is commonly used in everyday life, has a base of 10 and uses the digits 0 to 9 to represent numbers. Other examples of numeration systems include binary, octal, and hexadecimal, which are used in computer science and digital electronics.

## Instalation

There is no need to install, just download and use it in other programs. 
Also if you want to test you can run the test_change_system.py

```bash
python3 ./example/directory/test_change_system.py
```

To download

```bash
git clone https://github.com/um-computacion-tm/sistemas-de-numeracion-EVAnci
```

## How it works

There are many function to convert the numeration system you want to any other, but at the end all systems call two functions to work.
There are two main functions that can solve all, this functions are the following:

### decimal_wrapper(decimal, base)
This function recieves two parameters, a decimal number, and the base to convert to. Inside this functions there is a while loop to divide the number given by the base. This has an if conditional also, to change numbers to characters, in case the base is hexadecimal

### bin_oct_hex_to_decimal_wrapper(number, base)
This function also recieves two parameters. The a number in a random base, and the base of the number. Inside this function there is a for loop to convert any number into decimal.

## Usage

Just import the functions you need to your python program, or copy them into your program.

To import all copy the following:

```python
from change_base import *
```

## Contributors

Universidad de Mendoza

Author: Anci V. Elio Valentino (62197)
