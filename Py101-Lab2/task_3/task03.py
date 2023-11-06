def task(register):
    '''
    register -> dictionar
    return -> lista doar cu numele studentilor
    '''
    names = []

    ################### TO DO #########################
    f = lambda x: float(sum(register[x]) / len(register[x])) >= 8.5
    names = list(filter(f, register.keys()))
    ###################################################
    
    return names
