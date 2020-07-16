num = str(9119)
str_num = str(num)
first_digit = str_num[0]
second_digit = str_num[1]
third_digit = str_num[2]
fourth_digit = str_num[3]

first = int(first_digit)
square_first = first**2
first_str = str(square_first)

second = int(second_digit)
square_second = second**2
second_str = str(square_second)

third = int(third_digit)
square_third = third**2
third_str = str(square_third)

fourth = int(fourth_digit)
square_fourth = fourth**2
fourth_str = str(square_fourth)

numeros = first_str + second_str + third_str + fourth_str
integer = int(numeros)
print(integer)
