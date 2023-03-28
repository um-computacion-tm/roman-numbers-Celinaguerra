import unittest
def decimal_to_roman(decimal):

    u_mil=decimal
    if u_mil <=3999:
        totalmil = "M" * (u_mil//1000)
    centena = u_mil % 1000
    totalnum = totalmil
    
    if centena <=399:
        totalcentena = "C" * (centena//100)
    if centena >=400 and centena <= 499:
        totalcentena = "CD"
    if centena >=500 and centena <=899:
        totalcentena = "D" + "C"*((centena//100)-5)
    if centena >=900 and centena <=999:
        totalcentena = "CM"
    decena = centena % 100
    totalnum = totalnum + totalcentena

    if decena <=39:
        totaldecena = "X" * (decena//10)
    if decena >= 40 and decena <=49:
        totaldecena = "XL"
    if decena >= 50 and decena <=89:
        totaldecena = "L" + "X"*((decena//10)-5)
    if decena >= 90 and decena <=99:
        totaldecena = "XC"
    unidad = decena % 10
    totalnum = totalnum + totaldecena
    
    if unidad <=3:
        totalunidad = "I" * (unidad)
    if unidad == 4:
        totalunidad = "IV"
    if unidad >=5 and unidad <=8:
        totalunidad = "V" + "I"*(unidad-5)
    if unidad == 9:
        totalunidad = "IX"
    totalnum = totalnum + totalunidad

    return totalnum
        
    
class TestDecimalToRoman(unittest.TestCase):

    def test_1(self):
        resultado = decimal_to_roman(1)
        self.assertEqual(resultado,"I")
    
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

    def test_diez(self):
        resultado = decimal_to_roman(10)
        self.assertEqual(resultado,"X")

    def test_24(self):
        resultado = decimal_to_roman(24)
        self.assertEqual(resultado,"XXIV")
    
    def test_37(self):
        resultado = decimal_to_roman(37)
        self.assertEqual(resultado,"XXXVII")

    def test_94(self):
        resultado = decimal_to_roman(94)
        self.assertEqual(resultado,"XCIV")

    def test_105(self):
        resultado = decimal_to_roman(105)
        self.assertEqual(resultado,"CV")

    def test_207(self):
        resultado = decimal_to_roman(207)
        self.assertEqual(resultado,"CCVII")

    def test_462(self):
        resultado = decimal_to_roman(462)
        self.assertEqual(resultado,"CDLXII")

    def test_702(self):
        resultado = decimal_to_roman(702)
        self.assertEqual(resultado,"DCCII")

    def test_999(self):
        resultado = decimal_to_roman(999)
        self.assertEqual(resultado,"CMXCIX")
    
    def test_2500(self):
        resultado = decimal_to_roman(2500)
        self.assertEqual(resultado,"MMD")

    def test_3999(self):
        resultado = decimal_to_roman(3999)
        self.assertEqual(resultado,"MMMCMXCIX")

    def test_2584(self):
        resultado = decimal_to_roman(2584)
        self.assertEqual(resultado,"MMDLXXXIV")

    def test_2831(self):
        resultado = decimal_to_roman(2831)
        self.assertEqual(resultado,"MMDCCCXXXI")

if __name__=="__main__":
    unittest.main()

