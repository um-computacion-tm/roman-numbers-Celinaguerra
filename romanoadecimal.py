import unittest
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



class TestRomanToDecimal(unittest.TestCase):
    def test_I(self):
        resultado = roman_to_decimal("I")
        self.assertEqual(resultado,1)

    def test_III(self):
        resultado = roman_to_decimal("III")
        self.assertEqual(resultado,3)

    def test_IV(self):
        resultado = roman_to_decimal("IV")
        self.assertEqual(resultado,4)

    def test_V(self):
        resultado = roman_to_decimal("V")
        self.assertEqual(resultado,5)

    def test_VI(self):
        resultado = roman_to_decimal("VI")
        self.assertEqual(resultado,6)

    def test_CDXXXIV(self):
        resultado = roman_to_decimal("CDXXXIV")
        self.assertEqual(resultado,434)

    def test_MXI(self):
        resultado = roman_to_decimal("MXI")
        self.assertEqual(resultado,1011)

    def test_DLVIII(self):
        resultado = roman_to_decimal("DLVIII")
        self.assertEqual(resultado,558)



if __name__=="__main__":
    unittest.main()