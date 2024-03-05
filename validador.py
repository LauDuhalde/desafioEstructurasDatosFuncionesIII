
def validate(opciones, eleccion):
    """
    Valida que la opción escogida esté dentro de las opciones permitidas.
    ------------
    Parameter
    ------------
    opciones
        Type:   Array
        Ejemplo:    ['a', 'b', 'c', 'd']
    eleccion
        Type: String
        Posibles valores: letras o números
        Ejemplo:    [0, 1]
        
    Return
    ------------
    eleccion
        Type:   String
        Descripción:    Opción válida escogida
    """
    
    # Definir validación de eleccion
    ##########################################################################
    if eleccion not in opciones:
        while eleccion not in opciones:
            eleccion = input("Opción no válida, ingrese una de las opciones válidas: ").lower()
    ##########################################################################
    return eleccion


if __name__ == '__main__':
    
    eleccion = input('Ingresa una Opción: ').lower()
    # letras = ['a','b','c','d'] # pueden probar con letras también para verificar su funcionamiento.
    numeros = ['0','1']
    # Si se ingresan valores no validos a eleccion debe seguir preguntando
    validate(numeros, eleccion)
    
    
