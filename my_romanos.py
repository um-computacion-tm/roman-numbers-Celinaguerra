
def decimal_to_roman(number):

    u_mil=number
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
