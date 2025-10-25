# Calcular el interés de una cantidad
# Si se captura un interés de al menos 30%, se calcula
# Si el interes es menor, sólo se considera el monto

# 100         30%               0.3
# 200         29.999999%

quantity = float( input( "Captura la cantidad $: " ) )
interest = float( input( "Captura el interés %: " ) ) / 100
total = 0

if interest >= 0.3:
    # 10 + 5 * 2          30 No OK
    # 10 + 5 * 2          20 Sí OK
    total = quantity + ( quantity * interest )
    print( "El total con intereses es: ", total )
else:
    print( "El monto es: ", quantity )
