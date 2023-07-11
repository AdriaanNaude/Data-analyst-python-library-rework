def shape(list_a):

    convert = str(list_a)
    count = 0
    row = 0
    column = 0
    # gets row 
    for x in convert:
        if x == "[" or x == "]":
            count += 1
    if count == 2:
        row = int(count / 2)
    else:
        row = int((count - 2)/2)
    # gets column
    times = 0
    count = 0
    while times != row:
        
        if row == 1:
            column = len(list_a)
            times += 1
        else:
            count += len(list_a[times])
            times += 1

            column = int(count/row)
    
    result = (row, column)
    return result


