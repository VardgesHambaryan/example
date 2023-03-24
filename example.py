def func(lst: list) -> int:
    '''Return min value of list.'''
    if len(lst) == 1:
        return lst[0]
    if lst[0] > lst[-1]:
        lst[0] = lst[-1]
    return func(lst[:-1])

print(func([9,-1,5,-13,7,2]))