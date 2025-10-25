# 0802 String Occurrences
# Programa que lea una cadena y devuelva un diccionario con la cantidad de apariciones de cada carácter en la cadena.
# - Capturar cadena: "Lorem ipsum"
# - Devolver diccionario:  { "L": 1, "o": 5, ... "m": 2 }
#   - Apariciones de cada carácter en la cadena.

    # "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed quis mollis metus. Nunc euismod iaculis justo, gravida placerat elit congue eget. Aliquam aliquam quam et arcu auctor cursus. Cras tempor, mauris et blandit vehicula, nulla ante volutpat risus, a hendrerit purus libero at neque. Ut feugiat ligula eget augue mattis, vel tincidunt nibh sodales. Sed porttitor convallis ante ut fermentum. Pellentesque sed eros nisl."

phrase_string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed quis mollis metus. Nunc euismod iaculis justo, gravida placerat elit congue eget. Aliquam aliquam quam et arcu auctor cursus. Cras tempor, mauris et blandit vehicula, nulla ante volutpat risus, a hendrerit purus libero at neque. Ut feugiat ligula eget augue mattis, vel tincidunt nibh sodales. Sed porttitor convallis ante ut fermentum. Pellentesque sed eros nisl."
phrase_string = input( "Captura una frase: " )
phrase_chars = {}

for c in phrase_string:
    if not phrase_chars.get( c ):
        phrase_chars[ c ] = 1
    else:
        phrase_chars[ c ] = phrase_chars[ c ] + 1

print( phrase_chars )
