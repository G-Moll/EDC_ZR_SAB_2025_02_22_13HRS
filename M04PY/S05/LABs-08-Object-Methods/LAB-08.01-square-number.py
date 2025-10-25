# Trabajar con Diccionarios
# { "a": 10, "b": False, "c": [], "d": "Joshua", "e": {} }
# key/property : value

# Crear un diccionario para guardar los valores cuadrados
# las llaves serán valores consecutivos
# sus valores serán los cuadrados de las llaves
# { "1": 1, "2": 4, "3": 9, "4": 16, "5": 25 }
# capturar por consola, las cantidad de cuadrados a calcular

squared_numbers = {}
limit_keys = int( input( "Cuántos cuadrados quieres calcular: " ) )

for n in range( 1, limit_keys + 1 ): # 5 (6): 1 2 3 4 5
    squared_numbers[ str( n ) ] = n * n
    # squared_numbers[ "1" ] = 1
    # squared_numbers[ "3" ] = 9

print( squared_numbers )
