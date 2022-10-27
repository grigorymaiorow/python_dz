# Запись суммарного многочлена в строку.


def write_mnogochlen(sort_dict):
    str_mnogochlen = ""
    for k,val in sort_dict.items():
        my_str = f"{val}x^{k}+ "
        str_mnogochlen += my_str
    return str_mnogochlen