import unittest

def decimal_to_roman(decimal):
    if decimal <=3:
        return "I"*decimal
    elif decimal >5 and decimal <9:
        return "V" + "I"*(decimal-5)
    elif decimal == 5:
        return "V"
    elif decimal ==10:
        return "X"
    elif decimal == 4:
        return "IV"
    elif decimal == 9:
        return "IX"
    

class TestDecimalToRoman(unittest.TestCase):
    def test_uno(self):
        #pre condición
        ###NO HAY ###

        #proceso
        resultado = decimal_to_roman(1)

        #verificación
        self.assertEqual(resultado, 'I')
    
    def test_diez(self):
        resultado = decimal_to_roman(10)
        self.assertEqual(resultado,"X")

    def test_cinco(self):
        resultado = decimal_to_roman(5)
        self.assertEqual(resultado,"V")
    
    def test_dos(self):
        resultado = decimal_to_roman(2)
        self.assertEqual(resultado,"II")

    def test_tres(self):
        resultado = decimal_to_roman(3)
        self.assertEqual(resultado,"III")
    
    def test_seis(self):
        resultado = decimal_to_roman(6)
        self.assertEqual(resultado,"VI")
    
    def test_siete(self):
        resultado = decimal_to_roman(7)
        self.assertEqual(resultado,"VII")
    
    def test_ocho(self):
        resultado = decimal_to_roman(8)
        self.assertEqual(resultado, "VIII")
    
    def test_cuatro(self):
        resultado = decimal_to_roman(4)
        self.assertEqual(resultado, "IV")

    def test_nueve(self):
        resultado = decimal_to_roman(9)
        self.assertEqual(resultado,"IX")

if __name__=="__main__":
    unittest.main()

