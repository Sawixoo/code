
def narcissistic( value ):
    v = [int(a) for a in str(value)]
    l = len(v)
    res = 0
    for i in v:
        res += i ** l

    if res == value:
        return True
    else:
        return False


narcissistic(153)