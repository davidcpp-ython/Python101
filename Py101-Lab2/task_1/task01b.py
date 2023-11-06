def task1b(phrase):
    '''
    phrase -> string
    return -> string

    Transformati in litere mari vocalele din fraza
    si salvati rezultatul in "new_phrase"
    '''

    new_phrase = ""

    ################### TO DO #########################
    vowels = ['a', 'e', 'i', 'o', 'u']
    f = lambda x :  x.upper() if x in vowels else x

    new_phrase = list(map(f, phrase))

    ###################################################

    # Nu modificati valoarea de retur a functiei
    return ''.join(list(new_phrase))
