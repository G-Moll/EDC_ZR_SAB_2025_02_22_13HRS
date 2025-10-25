import random

list_numbers = []

for n in range( 1, 11 ):
    rand_number = random.randint( 1, 10 )
    print( "Número: ", rand_number )
    print( "Cuadrado: ", rand_number * rand_number )
    print( "Cubo: ", rand_number * rand_number * rand_number )
    list_numbers.append( rand_number )

print( list_numbers )
