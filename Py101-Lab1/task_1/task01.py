def func(note, nume_materie):
    """
    Trebuie sa creati un tuplu cu numele "pereche",
    in care veti tine, astfel, (media notelor, numele_materiei)
    exemplu: pereche = (...)
    """

    ################### TO DO #########################
    x = 0
    for i in note:
        x += i
    x = float(x/len(note))
    pereche = (x, nume_materie)
    ###################################################

    return pereche
