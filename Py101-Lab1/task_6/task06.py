def func(size):
    romb = ""

    ################### TO DO #########################
    if size % 2 == 0:
        n = size + 1
    else:
        n = size
    for i in range(int((n - 1) / 2)):
        for j in range(i, int((n - 1) / 2)):
            romb = romb + " "
        romb = romb + "@"
        for j in range(i):
            romb += ".."
        romb += "@\n"
    for i in range(int((n - 1) / 2) + 1):
        for j in range(i):
            romb = romb + " "
        romb = romb + "@"
        for j in range(i, int(((n - 1) / 2))):
            romb += ".."
        romb += "@\n"
    ###################################################

    return romb
