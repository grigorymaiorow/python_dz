# Делим строку по знаку "=" и складываем значения после него.


def posle_ravno(str):
    res = str.split("=")
    return(res[1])