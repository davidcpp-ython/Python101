def func(nume_complete):
    """
    Creeaza un tuplu "nume_formatat" care sa contina 3 elemente:
    nume_formatat[0] = lista cu numele de familie
    nume_formatat[1] = lista cu primele prenume
    nume_formatat[2] = lista cu celelalte prenume

    HINT!  conversie string - lista || (string.split("delimiter"))
    """


    ################### TO DO #########################
    fam = []
    p1 = []
    p2 = []

    for i in nume_complete:
        x = i.split(" ")
        fam.append(x[0])
        y = x[1].split("-")
        p1.append(y[0])
        p2.append(y[1])

    nume_formatat = (fam, p1, p2)
    ###################################################


    return nume_formatat

    