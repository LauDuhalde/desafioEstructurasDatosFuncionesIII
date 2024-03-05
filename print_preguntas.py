import preguntas as p
from string import ascii_uppercase

def print_pregunta(enunciado, alternativas):
    """
    Muestra en patalla el enunciado de la pregunta y sus alternativas.
    No tiene retorno.
    ------------
    Parameter
    ------------
    pregunta['enunciado']
        Type:   Array
        Ejemplo:    ['Enunciado básico 1']
    
    alternativas:
        Type:   Array
        Ejemplo:    [['alt_2', 0], 
                    ['alt_4', 1], 
                    ['alt_3', 0], 
                    ['alt_1', 0]] 
    """
    # Imprimir enunciado y alternativas
    ###############################################################
    for leer_enunciado  in enunciado:
        print(leer_enunciado)
    for i, alternativa in enumerate(alternativas):
        print(ascii_uppercase[i]+". "+alternativa[0])

    ###############################################################
        
if __name__ == '__main__':
    # Las preguntas y alternativas deben mostrarse según lo indicado
    pregunta = p.pool_preguntas['basicas']['pregunta_1']
    print_pregunta(pregunta['enunciado'],pregunta['alternativas'])
    
    # Enunciado básico 1

    # A. alt_1
    # B. alt_2
    # C. alt_3
    # D. alt_4