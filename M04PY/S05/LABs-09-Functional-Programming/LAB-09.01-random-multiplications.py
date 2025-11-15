# 0901 Random Multiplications
# Programa que pregunte aleatoriamente una multiplicación. El programa debe indicar si la respuesta ha sido correcta o no (en caso que la respuesta sea incorrecta el programa debe indicar cuál es la correcta). El programa preguntará 10 multiplicaciones, y al finalizar mostrará el número de aciertos.

# - Preguntar aleatoriamente una multiplicación
# - Indicar si la respuesta es correcta o no
#   - En caso que la respuesta sea incorrecta mostrar la correcta
# - Preguntar 10 multiplicaciones
# - Al finalizar mostrar aciertos

import random

def calculateMultiplication():
    # mult_calc = { "num_one": 2, "num_two": 4, "mult_nums": 8 }
    mult_calc = {}
    mult_calc[ "num_one" ] = random.randint( 1, 10 )
    mult_calc[ "num_two" ] = random.randint( 1, 10 )
    mult_calc[ "mult_nums" ] = mult_calc[ "num_one" ] * mult_calc[ "num_two" ]
    
    return mult_calc


def promptUser( fnData ):
    attempt_results = { "right": 0, "wrong": 0, "matches": [] }

    for t in range( 3 ):
        current_mult = fnData()
        num_one = current_mult[ "num_one" ] # 2 5
        num_two = current_mult[ "num_two" ] # 4 7
        mult_nums = current_mult[ "mult_nums" ] # 8

        string_msg = "Resultado de multiplicar " + str( num_one ) + " x " + str( num_two ) + ": "
        user_answer = int( input( string_msg ) )

        if user_answer != mult_nums:
            attempt_results[ "wrong" ] += 1
        else:
            attempt_results[ "right" ] += 1

        attempt_results[ "matches" ].append( { "pc": mult_nums, "user": user_answer, "matched": user_answer == mult_nums } )
    
    return attempt_results


def showResults( dataResults ):
    all_answers = ""
    all_answers += "Respuestas correctas: " + str( dataResults[ "right" ] )
    all_answers += "\nRespuestas incorrectas: " + str( dataResults[ "wrong" ] )
    all_answers += "\nRespuestas individuales"

    for m in dataResults[ "matches" ]:
        matched = ""
        if m[ "matched" ]:
            matched = "Sí"
        else:
            matched = "No"
        display_answer = "\n\tCorrecta: " + str( m[ "pc" ] ) + ", Usuario: "  + str( m[ "user" ] ) + ", Coinciden: " + matched
        all_answers += display_answer
    
    return all_answers


# all_results = promptUser()
# whole_message = showResults( all_results )
# print( whole_message )

print( showResults( promptUser( calculateMultiplication ) ) )

# funciones evaluadas           print()
# funciones referenciadas       print

# Programación Funcional
# 1) Cada función se encarga de realizar una tarea concreta
# 2) Las funciones pueden recibir datos (parámetros), y procesarlos internamente
    # - No deben tener dependencias externas
# 3) Las funciones deben de devolver un valor (explícito: return)

# value = 10
def sample( xyz ):
    return xyz * 8;

# result = sample()
# print( result )
# print( sample( 100 ) )

