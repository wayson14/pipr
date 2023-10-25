def every_third(l):
    l.reverse()
    l = l[1:]
    r = []
    for i in range(0, len(l), 3):
        r.append(l[i])
    return r

every_third([1, 2, 3, 4, 5, 6, 7, 8, 9])
pass
