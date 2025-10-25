# Lista de 5(00) cadenas, capturadas por teclado
# 5 cadenas por consola
# copiar en una segunda lista las cadenas, pero en sentido inverso: la primer cadena con última, la última como la primera

user_options = []
reverse_options = []

while len( user_options ) < 5:
    user_input = input( "Captura un valor: " )
    user_options.append( user_input )
    reverse_options.insert( 0, user_input )

print( user_options )
print( reverse_options )

