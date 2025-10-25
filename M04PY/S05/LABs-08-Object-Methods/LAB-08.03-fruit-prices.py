# 0803 Fruit Prices
# Programa donde se declare un diccionario para guardar los precios de las distintas frutas. El programa pedirá el nombre de la fruta y la cantidad que se ha vendido y nos mostrará el precio final de la fruta a partir de los datos guardados en el diccionario. Si la fruta no existe nos dará un error. Tras cada consulta el programa nos preguntará si queremos hacer otra consulta.
# Diccionario precios frutas
# Pedir nombre fruta
# Pedir cantidad vendida
# Mostrar costo final fruta (considerar datos del diccionario)
# Si la fruta no existe, mandar un mensaje
# Tras cada compra nos preguntará si queremos hacer otra más.

fruits_data = {}
fruits_data[ "apple" ] = 40
fruits_data[ "banana" ] = 20
fruits_data[ "blueberry" ] = 30
fruits_data[ "cherry" ] = 50
fruits_data[ "kiwi" ] = 40
fruits_data[ "mango" ] = 25
fruits_data[ "melon" ] = 20
fruits_data[ "orange" ] = 20
fruits_data[ "strawberry" ] = 30
fruits_data[ "tangerine" ] = 25
fruits_data[ "watermelon" ] = 25

while 1 == 1:
    fruit_choice = input( "Qué fruta quiere comprar: " )
    fruit_quantity: float
    fruit_price: float

    if fruit_choice not in fruits_data:
        print( "No tenemos disponible la fruta que seleccionaste." )
    else:
        fruit_quantity = float( input( "Cuánto quiere comprar: " ) )
        fruit_price = fruits_data[ fruit_choice ]
        print( "Fruta:", fruit_choice, ", Total: ", fruit_quantity * fruit_price )

    new_request_string = """
    ¿Quiere hacer alguna compra adicional?
    0) Salir de las compras
    1) Hacer una nueva compra
    """
    new_request = int( input( new_request_string ) )
    if new_request == 0:
        print( "Gracias por hacer sus compras..!" )
        break
    elif new_request == 1:
        continue
