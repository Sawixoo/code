def explode(arr):
    a , b = arr
    sum = 0
    if type(a) == str and type(b) == str:
        return 'Void!'
    for i in arr:
        if type(i) == int:
            sum += i
    
    return [arr] * sum
    

print(explode([1, 2]))
print(explode(['a', 3]))
print(explode([4, 'b']))
print(explode(['a', 'c']))