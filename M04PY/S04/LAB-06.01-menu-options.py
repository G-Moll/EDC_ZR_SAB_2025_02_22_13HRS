# Realizar un menú de donde se seleccionan distintas opciones, hasta que seleccionemos la opción de "Salir"
#                   0       1                   2       3
menu_options = [ "Café", "Huevos estrellados", "Pan", "Leche", "Chilaquiles", "Hot Cakes", "Jugo de Naranja", "Sandwich", "Postre" ]
choices = []

print( """
Seleccione alguna de las opciones del menú
1) Café             2) Huevos estrellados  3) Pan
4) Leche            5) Chilaquiles         6) Hot Cakes
7) Jugo de Naranja  8) Sandwich            9) Postre

0) Salir
""" )

while True:
    # 0,1,2,3... 90
    input_choice = int( input( "Escoge una opción del menú: " ) )
    
    if input_choice == 0:
        print( "Gracias por tus selecciones" )
        print( choices )
        break;
    elif input_choice >= 1 and input_choice <= 9:
        choices.append( menu_options[ input_choice - 1 ] )
    # elif input_choice == 1:
    #     choices.append( menu_options[ input_choice - 1 ] )
    # elif input_choice == 2:
    #     choices.append( menu_options[ input_choice - 1 ] )
    # elif input_choice == 3:
    #     choices.append( menu_options[ input_choice - 1 ] )
    # elif input_choice == 4:
    #     choices.append( menu_options[ input_choice - 1 ] )
    # elif input_choice == 5:
    #     choices.append( menu_options[ input_choice - 1 ] )
    # elif input_choice == 6:
    #     choices.append( menu_options[ input_choice - 1 ] )
    # elif input_choice == 7:
    #     choices.append( menu_options[ input_choice - 1 ] )
    # elif input_choice == 8:
    #     choices.append( menu_options[ input_choice - 1 ] )
    # elif input_choice == 9:
    #     choices.append( menu_options[ input_choice - 1 ] )
