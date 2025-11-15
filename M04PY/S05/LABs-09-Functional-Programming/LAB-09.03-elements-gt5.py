# 0903 Elements Greater than 5
# Obtener la cantidad de elementos mayores a 5 en la tupla.

# tupla = (5, 2, 6, 7, 8, 10, 77, 55, 2, 1, 30, 4, 2, 3)
tuple_data = ( 5, 2, 6, 7, 8, 10, 77, 55, 2, 1, 30, 4, 2, 3 )
number_edge = 5

def getUpperNumbers( listTuple, numEdge ):
    chosen_numbers = []

    for n in listTuple:
        if n > numEdge:
            chosen_numbers.append( n )

    return chosen_numbers

print( tuple_data )
print( getUpperNumbers( tuple_data, number_edge ) )
print( getUpperNumbers( tuple_data, 50 ) )
print( getUpperNumbers( tuple_data, 10 ) )
print( getUpperNumbers( tuple_data, 7 ) )
