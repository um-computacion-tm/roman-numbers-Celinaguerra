
def roman_to_decimal(roman):
    listaromanos = ["I", "V", "X", "L", "C", "D", "M"]
    listadecimales = [1, 5, 10, 50, 100, 500, 1000]
    decimal = 0
    anterior = 0

    for num in roman[::-1]:
        indice=listaromanos.index(num)
        if listadecimales[indice] >= anterior:
            decimal += listadecimales[indice]
        else:
            decimal -= listadecimales[indice]
        anterior = listadecimales[indice]
    return decimal
