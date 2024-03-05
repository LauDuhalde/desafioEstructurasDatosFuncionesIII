##Valores pre definidos para pruebas

"""preguntas_basicas = {
    'pregunta_1': {'enunciado':['Enunciado básico 1'],
    'alternativas': [['alt_1', 0], 
                     ['alt_2', 1], 
                     ['alt_3', 0], 
                     ['alt_4', 0]]},
    'pregunta_2': {'enunciado':['Enunciado básico 2'],
    'alternativas': [['alt_1', 0], 
                     ['alt_2', 1], 
                     ['alt_3', 0], 
                     ['alt_4', 0]]},
    
'pregunta_3': {'enunciado':['Enunciado básico 3'],
    'alternativas': [['alt_1', 0], 
                     ['alt_2', 1], 
                     ['alt_3', 0], 
                     ['alt_4', 0]]}
}

preguntas_intermedias = {
    'pregunta_1': {'enunciado':['Enunciado intermedio 1'],
    'alternativas': [['alt_1', 0], 
                     ['alt_2', 1], 
                     ['alt_3', 0], 
                     ['alt_4', 0]]},
    'pregunta_2': {'enunciado':['Enunciado intermedio 2'],
    'alternativas': [['alt_1', 0], 
                     ['alt_2', 1], 
                     ['alt_3', 0], 
                     ['alt_4', 0]]},
    
'pregunta_3': {'enunciado':['Enunciado intermedio 3'],
    'alternativas': [['alt_1', 0], 
                     ['alt_2', 1], 
                     ['alt_3', 0], 
                     ['alt_4', 0]]}
}

preguntas_avanzadas = {
    'pregunta_1': {'enunciado':['Enunciado avanzado 1'],
    'alternativas': [['alt_1', 0], 
                     ['alt_2', 1], 
                     ['alt_3', 0], 
                     ['alt_4', 0]]},
    'pregunta_2': {'enunciado':['Enunciado avanzado 2'],
    'alternativas': [['alt_1', 0], 
                     ['alt_2', 1], 
                     ['alt_3', 0], 
                     ['alt_4', 0]]},
    
'pregunta_3': {'enunciado':['Enunciado avanzado 3'],
    'alternativas': [['alt_1', 0], 
                     ['alt_2', 1], 
                     ['alt_3', 0], 
                     ['alt_4', 0]]}
}"""


##Trivia real
preguntas_basicas = {
    'pregunta_1': {
        'enunciado': ['¿Cuál es la capital de Francia?'],
        'alternativas': [
            ['Madrid', 0], 
            ['París', 1], 
            ['Roma', 0], 
            ['Londres', 0]
        ]
    },
    'pregunta_2': {
        'enunciado': ['¿Quién pintó la Mona Lisa?'],
        'alternativas': [
            ['Vincent van Gogh', 0], 
            ['Leonardo da Vinci', 1], 
            ['Pablo Picasso', 0], 
            ['Salvador Dalí', 0]
        ]
    },
    'pregunta_3': {
        'enunciado': ['¿En qué año comenzó la Segunda Guerra Mundial?'],
        'alternativas': [
            ['1939', 1], 
            ['1914', 0], 
            ['1945', 0], 
            ['1950', 0]
        ]
    }
}

preguntas_intermedias = {
    'pregunta_1': {
        'enunciado': ['¿Cuál es el río más largo del mundo?'],
        'alternativas': [
            ['Amazonas', 1], 
            ['Nilo', 0], 
            ['Yangtsé', 0], 
            ['Misisipi', 0]
        ]
    },
    'pregunta_2': {
        'enunciado': ['¿Cuál es el metal más abundante en la corteza terrestre?'],
        'alternativas': [
            ['Oro', 0], 
            ['Hierro', 1], 
            ['Plata', 0], 
            ['Aluminio', 0]
        ]
    },
    'pregunta_3': {
        'enunciado': ['¿Cuál es el planeta más grande del Sistema Solar?'],
        'alternativas': [
            ['Mercurio', 0], 
            ['Venus', 0], 
            ['Júpiter', 1], 
            ['Saturno', 0]
        ]
    }
}

preguntas_avanzadas = {
    'pregunta_1': {
        'enunciado': ['¿Quién escribió "El Quijote"?'],
        'alternativas': [
            ['Miguel de Cervantes', 1], 
            ['William Shakespeare', 0], 
            ['Franz Kafka', 0], 
            ['Gabriel García Márquez', 0]
        ]
    },
    'pregunta_2': {
        'enunciado': ['¿Cuál es el metal más ligero?'],
        'alternativas': [
            ['Oro', 0], 
            ['Plata', 0], 
            ['Aluminio', 0], 
            ['Litio', 1]
        ]
    },
    'pregunta_3': {
        'enunciado': ['¿En qué año se fundó la ONU?'],
        'alternativas': [
            ['1945', 1], 
            ['1919', 0], 
            ['1950', 0], 
            ['1930', 0]
        ]
    }
}



pool_preguntas = {'basicas': preguntas_basicas,
                  'intermedias': preguntas_intermedias,
                  'avanzadas': preguntas_avanzadas}