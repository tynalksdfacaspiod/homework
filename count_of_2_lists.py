list1 = [0,33,37,6,10,44,13,47,16,18,22,25]
list2 = [1,38,48,8,41,7,12,47,16,40,20,23,25]

def f(list1, list2):
    count_dbl = 0
    if len(list2) >= len(list1):
        for i in list2:
            if i in list1:
                count_dbl += 1
    else:
        for i in list1:
            if i in list2:
                count_dbl += 1

    count_unique = 0
    for i in list2:
        if i not in list1:
            count_unique+=1
    for i in list1:
        if i not in list2:
            count_unique+=1

    len1 = len(list1)
    len2 = len(list2)
    for i in range(len1):
        if list1[i] in list2:
            len1-=1

    for i in range(len2):
        if list2[i] in list1:
            len2 -= 1
    print(count_dbl, count_unique, len1, len2)

f(list1, list2)
