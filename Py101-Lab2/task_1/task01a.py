def task1a(nums):
    '''
    nums -> vector int
    return -> vector int

    Dublati elementele care se divid cu 6, iar pe cele 
    care nu se divid, triplati-le folosind functionale
    '''

    result = []

    ################### TO DO #########################
    # def f(num):
    #     if num % 6 == 0:
    #         return num * 2
    #     else:
    #         return num * 3
    f = lambda num : num * 2 if num % 6 == 0 else num * 3
    result = list(map(f, nums))
    ###################################################

    # Nu modificati valoarea de retur a functiei
    return list(result)
