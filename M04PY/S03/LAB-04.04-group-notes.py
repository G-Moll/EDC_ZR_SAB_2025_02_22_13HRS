# Guardar info
    # Guardar nombres de alumnos
    # Guardar notas de cada
# Cada alumno tiene una cantidad distinta de notas
    # Usar diccionarios (llaves: nombres, valores las notas)
# sg = {
#     "joshua": [ 10 , 20, 8, 12 ],
#     "peter": [ 20 , 5 ]
# }
# sg[ "paul" ] = [ 7,3,15 ];
# sg[ "irene" ] = [ 3, 7,3,10 ];

# print( sg )
# st = "joshua"
# st = "peter"
# print( sg[ st ][ 2 ] )
# print( sg[ "peter"  ] )

# La app pide la cantidad de alumnos a capturar
    # Nombre
    # Notas

# App muestra:
    # lista de alumnos
    # el promedio de cada alumno

# Consideración: ver si ya existe el alumno


students_group = {}
students_quantity = int( input( "Número de alumnos: " ) )

# ====================================
# Capturar datos
for student in range( students_quantity ):
    print( "Estudiante: " + str( student + 1 ) )
    current_name = input( "Nombre: " )
    current_notes = []
    students_group[ current_name ] = current_notes
    
    while True:
        current_note = float( input( "Captura la Nota: " ) )
        if current_note < 0:
            break
        elif current_note >= 0 and  current_note <= 10:       
            current_notes.append( current_note )

# ====================================
# Mostrar datos
# students_group = {
#     "joshua": [ 10 , 20, 8, 12 ],
#     "peter": [ 20 , 5 ],
#     "andrew": [ 20 , 5, 7 ],
#     "paul": [ 20, 8, 12 ]
# }
# print( students_group )


for current_student in students_group:
    print( "Notas de " + current_student )
    current_notes_quantity = len( students_group[ current_student ] )
    print( "Número de notas: " + str( current_notes_quantity ) )
    print( "Notas: " + str( students_group[ current_student ] ) )
    avg = sum( students_group[ current_student ] ) / current_notes_quantity
    print( "Promedio: " + str( avg ) + "\n" )





        # Validaciones de las notas
        # 6.8: >= 0  o <=10  No-OK
        # 11.8: >= 0  o <=10 No-OK
        # 11.8: >= 0  y <=10 OK
    # 00000
        # 0 - 10
        # - 10
        # pass
