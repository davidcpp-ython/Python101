def task(*args):
    '''
    args -> elemente de tipuri diferite
    return -> lista cu elementele corespunzatoare
    '''

    result = []

    ################### TO DO #########################
    # s = ['a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U']
    # s = "bcdfghjklmnpqrstvwxyz"
    # for x in args:
    #     if type(x) == int:
    #         result.append(x)
    #     elif type(x) == str and s.find(x) != -1 and len(x) == 1:
    #         result.append(x)
    f = lambda x: type(x) == int or(type(x) == str and len(x) == 1 and x not in "aeiou" and x >='a' and x <='z')
    result = list(filter(f, args))
    ###################################################
    
    return result
