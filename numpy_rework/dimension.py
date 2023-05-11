def ndim(list_a):

    convert = str(list_a)
    count = 0
    dimension = 0
    for x in convert:
        if x == "[" or x == "]":
            count += 1
    if count == 2:
        dimension = count / 2
    else:
        dimension = int((count - 2)/2)

    return dimension

        
