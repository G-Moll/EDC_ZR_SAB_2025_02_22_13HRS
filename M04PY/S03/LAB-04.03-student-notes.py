# Capturar 5 calificaciones
# Notas entre 1 y 10
# Mostrar:
    # Nota más baja
    # Nota más alta
    # Promedio

student_notes = []

while len( student_notes ) < 5:
    current_note = float( input( "Captura una nota: " ) )
    if current_note >= 0 and current_note <= 10:
        student_notes.append( current_note )

print( "Calificaciones", student_notes )
print( "Promedio", sum( student_notes ) / len( student_notes ) )
print( "Máxima", max( student_notes ) )
print( "Mínima", min( student_notes ) )
