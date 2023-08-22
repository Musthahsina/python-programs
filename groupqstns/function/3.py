'''prgram to print odd numbers from a list'''

def odd_num(list):
    onum = []
    for i in list:
        if i % 2 != 0:
            onum.append(i)
    return onum
print(odd_num([1, 2, 3, 4, 5, 6, 7, 8, 9]))
