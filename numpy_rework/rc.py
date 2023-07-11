import numpy_rework.dimension as nd

# find item based on r = row and c = columm

def rc(list_a, r=0, c=0):
    x = nd.ndim(list_a)
    if x == 1:
        result = list_a[c]
    else:
        result = list_a[r][c]
    return result
