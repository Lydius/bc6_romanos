simbolos= {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}

def romano_a_entero(romano):
    
    if isinstance(romano, str) and romano.upper() in simbolos:
        return simbolos[romano.upper()]
    elif isinstance(romano, str):
        raise ValueError("No permitido")
    else:
        raise ValueError("Tiene que ser un string")
