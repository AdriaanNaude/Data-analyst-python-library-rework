import numpy_rework.dimension as nd
def size(list_a):

    count = 0
    row_Count = nd.ndim(list_a)
    element = 0
    while count != row_Count:
        if row_Count == 1:
            element = len(list_a)
            count += 1
        else:
            x = len(list_a[count])
            element += x
            count += 1

    return element
