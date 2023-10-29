def zig_zag(rows, cols):

    zig_zag_matrix = []

    ################### TO DO #########################
    x = 0
    y = 1
    for i in range(rows):
        for j in range(cols):
            l = [0 for i in range(cols)]
            l[x] = 1
            zig_zag_matrix.append(l)
            if x == 0:
                y = 1
            elif x == cols - 1:
                y = -1
            x += y

    ###################################################

    return zig_zag_matrix
