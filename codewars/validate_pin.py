import re


def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()

print(validate_pin('aa1234'))
print(validate_pin('-111234'))
print(validate_pin('23'))
print(validate_pin('2323'))
print(validate_pin('gggg'))
