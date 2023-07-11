
# multiply all items in a list with items of another list

def mul_list(list_a, list_b):
    newlist = []
    times = 0
    length_List1 = len(list_a) 
    length_List2 = len(list_b)

    if length_List1 != length_List2:
        return "list a and list b not same length"

    while times != length_List1:
        # read list a 
        def read_a(list_a):
            for x in list_a:
                return x
        # read list b 
        def read_b(list_b):
            for y in list_b:
                return y
        # multiply list a with b 
        result = lambda x, y: x * y
        newlist.append(result(read_a(list_a), read_b(list_b)))
        times += 1
        # reverse list pop of first item (now last) and reverse back, 
        # now second item is first
        list_a.reverse()
        list_a.pop()
        list_a.reverse()

        list_b.reverse()
        list_b.pop()
        list_b.reverse()

    return newlist

# sum of all items in a list with items of another list

def sum_list(list_a, list_b):
    newlist = []
    times = 0
    length_List1 = len(list_a) 
    length_List2 = len(list_b)

    if length_List1 != length_List2:
        return "list a and list b not same length"

    while times != length_List1:
        # read list a 
        def read_a(list_a):
            for x in list_a:
                return x
        # read list b 
        def read_b(list_b):
            for y in list_b:
                return y
        # multiply list a with b 
        result = lambda x, y: x + y
        newlist.append(result(read_a(list_a), read_b(list_b)))
        times += 1
        # reverse list pop of first item (now last) and reverse back, 
        # now second item is first
        list_a.reverse()
        list_a.pop()
        list_a.reverse()

        list_b.reverse()
        list_b.pop()
        list_b.reverse()

    return newlist

# subtract all items in a list with items of another list

def subt_list(list_a, list_b):
    newlist = []
    times = 0
    length_List1 = len(list_a) 
    length_List2 = len(list_b)

    if length_List1 != length_List2:
        return "list a and list b not same length"

    while times != length_List1:
        # read list a 
        def read_a(list_a):
            for x in list_a:
                return x
        # read list b 
        def read_b(list_b):
            for y in list_b:
                return y
        # multiply list a with b 
        result = lambda x, y: x - y
        newlist.append(result(read_a(list_a), read_b(list_b)))
        times += 1
        # reverse list pop of first item (now last) and reverse back, 
        # now second item is first
        list_a.reverse()
        list_a.pop()
        list_a.reverse()

        list_b.reverse()
        list_b.pop()
        list_b.reverse()

    return newlist

# divide all items in a list with items of another list

def div_list(list_a, list_b):
    newlist = []
    times = 0
    length_List1 = len(list_a) 
    length_List2 = len(list_b)

    if length_List1 != length_List2:
        return "list a and list b not same length"

    while times != length_List1:
        # read list a 
        def read_a(list_a):
            for x in list_a:
                return x
        # read list b 
        def read_b(list_b):
            for y in list_b:
                return y
        # multiply list a with b 
        result = lambda x, y: x / y
        newlist.append(result(read_a(list_a), read_b(list_b)))
        times += 1
        # reverse list pop of first item (now last) and reverse back, 
        # now second item is first
        list_a.reverse()
        list_a.pop()
        list_a.reverse()

        list_b.reverse()
        list_b.pop()
        list_b.reverse()

    return newlist


