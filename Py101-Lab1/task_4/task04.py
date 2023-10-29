def func(given_numbers):
    ################### TO DO #########################

    # Completeaza doar linia urmatoare
    nice_list = [tuple([i ** j for j in range(1,4)])for i in given_numbers if i < 100 if i % 2==0 or i % 3==0]
    ###################################################

    return nice_list
