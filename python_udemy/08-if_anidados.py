lenguajes = ['Python', 'Kotlin', 'Java', 'Javascript']

if 'PHP' in lenguajes:
    print('PHO si existe')
else: 
    print('No esta en la lista')
    
#if anidado
usuario_autentificado = True
usuario_admin = True

if usuario_autentificado: #true
    if usuario_admin: #true 
       print('ACCESO TOTAL')
    else:
        print('Acceso al sistema')
else:
    print('Debes iniciar sesión')