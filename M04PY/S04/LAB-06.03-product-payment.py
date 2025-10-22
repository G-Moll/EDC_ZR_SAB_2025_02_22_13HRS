# Calcular los pagos de un producto durante 20 meses
# El primer mes se paga     $10                 $30
# El segundo mes se paga    $20                 $60
# El tercer mes se paga     $40                 $120
# y así sucesivamente       $80, $160, $320

# Calcular el pago mensual
# Calcular el pago total

base_payment = 10
current_payment = 0      # 10, 20, 40, 80
total_payment = 0        # 10, 30, 70

for n in range( 1, 21 ):
    if n == 1:
        current_payment = base_payment
    else:
        current_payment = current_payment * 2
    total_payment += current_payment
    print( "Pago del mes", n ,current_payment )
print( "Pago total", total_payment )

