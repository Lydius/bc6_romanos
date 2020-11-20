simbolos = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
tipo5 = {'V', 'D', 'L'}
tipo1 = {'I','X', 'C', 'M'}
restas_par = {'CD','CM', 'XL', 'XC', 'IV', 'IX'}

def simbolo_a_entero(simbolo):
    if isinstance(simbolo, str) and simbolo.upper() in simbolos:
        return simbolos[simbolo.upper()]
    elif isinstance(simbolo, str):
        raise ValueError("No permitido")
    else:
        raise ValueError("Tiene que ser un string")

def romano_a_entero(romano):

    if not isinstance(romano,str):
        raise ValueError("Tiene que ser un string")

    suma = 0
    c_repes = 0
    valor_anterior = ""

    for letra in romano: 
        if letra == valor_anterior and letra in tipo5: 
            raise OverflowError("Demasiados simbolos tipo 5")
        if letra == valor_anterior: 
            c_repes += 1
            if c_repes > 2:
                raise OverflowError("Demasiados simbolos tipo 1")
        elif valor_anterior and simbolo_a_entero(letra) > simbolo_a_entero(valor_anterior):
            if valor_anterior+letra not in restas_par:
                raise ValueError("No se puede restar")
            suma -= simbolos[valor_anterior]*2 
            c_repes = 0
        else:
            c_repes = 0

        suma += simbolo_a_entero(letra)
        valor_anterior = letra
    return suma
