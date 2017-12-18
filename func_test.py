def get_long(a):
    print len(a)
    return get_long(a+a)

get_long('qwertyuioplkjhgfdsazxcvbnm')