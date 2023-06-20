def descending_order(num):
    x = [x for x in str(num)]
    x.sort(reverse = True)
    return int(''.join(x))

print(descending_order(123456789))