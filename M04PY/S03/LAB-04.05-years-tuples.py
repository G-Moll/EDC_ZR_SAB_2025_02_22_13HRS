# Tupla con meses del año
# Solicita al usuario un número
# si ese número está entre 1 y la longitud de la tupla 1, 6 , 12
# mostramos esa cantidad de elementos
# ( "Ene", "Feb", "Mar", ....5, 5, 6, 40 )



print( """
0) Salir
1-12) Mostra mes
""")
# User      1       2    3      4
# Python    0       1    2      3
months = ( "Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic" )

while True:
    user_option = int( input( "Mostrar mes: " ) )
    print( "Opción: " + str( user_option ) )

    if( user_option < 1 and user_option > len( months ) ):
        print( "Opción no válida..." )
        break
    else:
        print( months[ user_option - 1 ] )



# print( "\tuna \"tabulación\" \n\tun salto de línea" );
