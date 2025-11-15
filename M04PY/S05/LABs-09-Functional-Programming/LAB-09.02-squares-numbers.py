# 0902 Square Numbers
# Obtener el cuadrado de todos los elementos en la lista.

# Lista: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# Lista: 6, 18, 9, 20
list_one = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
list_two = [ 6, 18, 9, 20 ]

def squareNumbers( listNumbers ):
    squared_numbers = []

    for n in listNumbers:
        squared_numbers.append( n * n )

    return squared_numbers

print( squareNumbers( list_one ) )
print( squareNumbers( list_two ) )
print( squareNumbers( [ 3, 6, 18, 8, 28 ] ) )
