def double_print(string):
    if string != '':
        print(string)
        print(string)
    else:
        raise ValueError('empty string is not allowed')


double_print('')
