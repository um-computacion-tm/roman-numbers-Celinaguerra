import unittest
def decimal_to_roman(decimal):

################ VARIABLES ##################

    totaldecimal = ""

    if decimal == 50:
        return "L"
    elif decimal == 100:
        return "C"
    elif decimal == 500:
        return "D"
    elif decimal == 1000:
       return "M"


############### 1-39 ####################

    if decimal > 10 and decimal < 40:
        totaldecimal = "X" * (decimal //10)
        decimal = decimal % 10
    if decimal <=3:
        return totaldecimal + "I"*decimal    
    elif decimal == 5:
        return totaldecimal + "V"
    elif decimal >5 and decimal <9:                                 #recordatorio para cambiar nombres de variables
        return totaldecimal + ("V" + "I"*(decimal-5))                           #para evitar confusiones
    elif decimal ==10:
        return totaldecimal + "X"
    if decimal == 4:
        return totaldecimal + "IV"
    if decimal == 9:
        return totaldecimal + "IX"
    
############ algunas centenas #############

    num = ""
    if decimal >= 100:
        centena = decimal // 100
        num = 'C' * centena
        decimal = decimal % 100 
    if decimal <= 3:
        num += 'I' * decimal
    elif decimal == 5:
        num += 'V'
    elif decimal == 10:
        num += "X"
    elif decimal >5 and decimal <9:
        num += "V" + "I"*(decimal-5)  
    return num



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
    
    def test_24(self):
        resultado = decimal_to_roman(24)
        self.assertEqual(resultado,"XXIV")
    
    def test_37(self):
        resultado = decimal_to_roman(37)
        self.assertEqual(resultado,"XXXVII")

    def test_105(self):
        resultado = decimal_to_roman(105)
        self.assertEqual(resultado,"CV")

    def test_207(self):
        resultado = decimal_to_roman(207)
        self.assertEqual(resultado,"CCVII")

if __name__=="__main__":
    unittest.main()

