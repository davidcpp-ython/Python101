def task1c(words):
    '''
    words -> lista string-uri
    return -> lista string-uri

    Salvati cuvintele care sunt palindrom in "palindromes"
    '''

    palindromes = []

    ################### TO DO #########################

    f = lambda w : True if w == w[::-1] else False
    palindromes = list(filter(f, words))
    ###################################################

    # Nu modificati valoarea de retur a functiei
    return list(palindromes)
