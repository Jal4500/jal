def verificar_temp(temp):
    if  temp > 15:
        print('Usa un abrigo y bufanda')
    elif temp > 25 and temp <= 35:
        print('Usa un abrigo')
    elif temp < 35:
        print('Deja el abrigo en casa')
