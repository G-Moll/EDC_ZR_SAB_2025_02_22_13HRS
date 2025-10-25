# Imprimir si un número es - ó +
current_number = int( input( "Captura un número: " ) )

# if current_number >= 0:
#     print( "El número es positivo: ", current_number )
# else:
#     print( "El número es negativo: ", current_number )

if current_number > 0:
    print( "El número es positivo: ", current_number )
elif current_number < 0:
    print( "El número es negativo: ", current_number )
else:
    print( "El número es el valor neutro: ", current_number )

