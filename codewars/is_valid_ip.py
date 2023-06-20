import re
from ipaddress import ip_address


def is_valid_IP(strng):
    # Работает не правильно
    # result = re.match('^([01]?\d\d?|2[0-4]\d|25[0-5])\.([01]?\d\d?|2[0-4]\d|25[0-5])\.([01]?\d\d?|2[0-4]\d|25[0-5])\.([01]?\d\d?|2[0-4]\d|25[0-5])$', strng)
    # return result != None

    try:
        return True if ip_address(strng) else False
    except:
        return False



print(is_valid_IP('12.255.56.1'))
print(is_valid_IP(''))
print(is_valid_IP('abc.def.ghi.jkl'))
print(is_valid_IP('253.134.249.242ab'))