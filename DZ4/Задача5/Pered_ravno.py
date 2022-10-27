# Берём то, что стоит слева от равно и делим по знаку +.


def pered_ravno(my_str):
    res = my_str.split("=")
    return(res[0])