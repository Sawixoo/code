def get_middle(s):
    mid = len(s)//2
    if len(s) % 2 != 0:
        return s[mid]
    else:
        return s[mid-1:mid+1]

print(get_middle('aabaa'))
print(get_middle('aabbaa'))
    