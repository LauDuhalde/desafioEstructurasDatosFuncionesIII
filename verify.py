import preguntas as p


def verificar(alternativas, eleccion):
    """
    Valida que la opción escogida sea la respuesta correcta a la pregunta.
    ------------
    Parameter
    ------------
    alternativas
        Type:   Array
        Ejemplo:    [['alt_2', 0], 
                    ['alt_4', 1], 
                    ['alt_3', 0], 
                    ['alt_1', 0]]
    eleccion
        Type: String
        Posibles valores: 'a', 'b', 'c', 'd' 
        
    Return
    ------------
    correcto
        Type:   Boolean
        Ejemplo:    Respuesta correcta = True
                    Respuesta incorrecta = False
    """
    #devuelve el índice de elección dada
    eleccion = ['a', 'b', 'c','d'].index(eleccion)
    correcto = False

    # generar lógica para determinar respuestas correctas
    ##########################################################################################
    if alternativas[eleccion][1]==1:
        print("Respuesta Correcta")
        correcto = True
    else:
        print("Respuesta Incorrecta")
        correcto = False

    
    
    
    ##########################################################################################
    return correcto



if __name__ == '__main__':
    from print_preguntas import print_pregunta
    
    # Siempre que se escoja la alternativa con alt_2 estará correcta, e incorrecta en cualquier otro caso
    pregunta = p.pool_preguntas['basicas']['pregunta_2']
    print_pregunta(pregunta['enunciado'],pregunta['alternativas'])
    respuesta = input('Escoja la alternativa correcta:\n> ').lower()
    verificar(pregunta['alternativas'], respuesta)






