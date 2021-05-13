def run():
    mi_diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    }
    # print(mi_diccionario['llave1'])
    # print(mi_diccionario['llave2'])
    # print(mi_diccionario['llave3']) 
    
    poblacion_paises={
        'argentina': 7228282,
        'brasil': 338833,
        'chile' : 2873833
    }
    
    # print(poblacion_paises['brasil'])
    
    for pais in poblacion_paises.keys():
        print(pais)
    
    for pais in poblacion_paises.values():
        print(pais)
        
        
    poblacion={
        'argentina': 7228282,
        'brasil': 338833,
        'chile' : 2873833
    }
    for pais,poblacion in poblacion.items():
        print(pais + ' tiene ' + str(poblacion) + ' habitantes')

if __name__ == '__main__':
    run()