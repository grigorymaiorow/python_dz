from random import choice


def filling(str):
    my_dict = \
    {
        'x1y1' : '' , 'x2y1' : ''  , 'x3y1' : '' ,
        'x1y2' : '' , 'x2y2' : ''  , 'x3y2' : '' ,
        'x1y3' : '' , 'x2y3' : ''  , 'x3y3' : ''
    }
    for key in my_dict:
        my_dict[key] = choice(str)
    return my_dict
