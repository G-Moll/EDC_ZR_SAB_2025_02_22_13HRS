# 0904 List Sum
# Obtener la suma de todos los elementos en la lista.
list_data = [ 5, 2, 6, 7, 8, 10, 77, 55, 2, 1, 30, 4, 2, 3 ]

def sumList( listData ):
    list_sum = 0

    for n in listData:
        list_sum += n

    return list_sum

print( sumList( list_data ) )
print( sumList( [ 1, 2, 30, 45 ] ) )
