
def find_it(seq):
    return [x for x in seq if seq.count(x) % 2 == 1][0]

print(find_it([1,2,2,3,3,3,4,3,3,3,2,2,1]))