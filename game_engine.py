import random


def random_values():
    a = random.randrange(1, 9)
    b = random.randrange(0, 9)
    c = random.randrange(0, 9)
    d = random.randrange(0, 9)
    return str(a) + str(b) + str(c) + str(d)


def check_values(list, input):
    i = 0
    v = 0
    i_2 = 0
    f_2 = 0
    for values, in list:
        f = 0
        for figure in input:
            if values == figure and v == f:
                i += 1
                f += 1
            else:
                f += 1
                if values == figure:
                    f_2 += 1
        if f_2 > 0 and v != f:
            i_2 += 1
            f_2 = 0
        else:
            f_2 = 0
        v += 1
    male = i
    female = i_2 - i
    if female < 0 or male == 3:
        female = 0
    return male, female

