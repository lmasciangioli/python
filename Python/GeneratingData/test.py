def square_digits(num):
    numeros = []
    str_num = str(num)
    first_digit = str_num[0]
    numeros.append(first_digit)
    second_digit = str_num[1]
    numeros.append(second_digit)
    third_digit = str_num[2]
    numeros.append(third_digit)
    fourth_digit = str_num[3]
    numeros.append(fourth_digit)

    cadena = []
    for digit in numeros:
        int(digit)
        cadena.append(digit)

