# Calcular números factoriales
# 2!  1x2               2
# 3!  1x2x3             6
# 4!  1x2x3x4           24
# 5!  1x2x3x4x5         120
# 6!  1x2x3x4x5x6       720

factorial_input = int( input( "Captura un entero: " ) )
factorial_result = 0
current_calculation = 1 # 2, 6, 24

if factorial_input > 0:
    for n in range( 1, factorial_input + 1 ):
        current_calculation = current_calculation * n
        # print( current_calculation )
    print( current_calculation )
elif factorial_input == 0:
    print( "Factorial de cero es 1" )
