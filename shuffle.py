import preguntas as p
import random

def shuffle_alt(pregunta):
    """
    Devuelve las alternativas mezcladas de forma random.
    ------------
    Parameter
    ------------
    pregunta
        Type:   Diccionario
        Ejemplo:    {'enunciado':['Enunciado básico 1'],
                        'alternativas': [['alt_1', 0], 
                            ['alt_2', 1], 
                            ['alt_3', 0], 
                            ['alt_4', 0]]}
    Return
    ------------
    alternativas
        Type:   Array
        Ejemplo:    [['alt_1', 0], 
                    ['alt_2', 1], 
                    ['alt_3', 0], 
                    ['alt_4', 0]]
    """
    #mezclar alternativas
    #######################################################################
    
    random.shuffle(pregunta['alternativas'])

    #######################################################################
    
    return pregunta['alternativas']

if __name__ == '__main__':
    # si se ejecuta el  programa varias veces las alternativas debieran aparecer en distinto orden
    print(shuffle_alt(p.pool_preguntas['basicas']['pregunta_1'])) 
    # a modo de ejemplo
    # [['alt_1', 0], ['alt_3', 0], ['alt_2', 1], ['alt_4', 0]]