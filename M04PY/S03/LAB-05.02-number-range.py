# Mostrar en pantalla si el número capturado está en el rango de 1 a 7
current_number = int( float( input( "Captura un número: " ) ) )

if current_number >= 1 and current_number <= 7:
    print( "Sí está dentro del rango:", current_number )
else:
    print( "No está dentro del rango:", current_number )
