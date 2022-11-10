my_dict = \
     {'x1y1' : 'x', 'x2y1' : 'x', 'x3y1' : '0', 
      'x1y2' : 'x', 'x2y2' : '0', 'x3y2' : '0', 
      'x1y3' : '0', 'x2y3' : '0', 'x3y3' : 'x'
     }

def who_win(my_dict):
    if (   my_dict['x1y1'] == my_dict['x2y1'] == my_dict['x3y1']
        or my_dict['x1y1'] == my_dict['x1y2'] == my_dict['x1y3']
        or my_dict['x1y1'] == my_dict['x2y2'] == my_dict['x3y3']
        ):

        return my_dict['x1y1']


    if (   my_dict['x1y2'] == my_dict['x2y2'] == my_dict['x3y2']
        or my_dict['x1y3'] == my_dict['x2y2'] == my_dict['x3y1']
        or my_dict['x2y1'] == my_dict['x2y2'] == my_dict['x2y3']
        ):

        return my_dict['x2y2']

    if (   my_dict['x1y3'] == my_dict['x2y3'] == my_dict['x3y3']
        or my_dict['x3y1'] == my_dict['x3y2'] == my_dict['x3y3']
        ):

        return my_dict['x3y3']



        
        