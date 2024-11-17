# Password generator

import random,time
while True:
    print("Vis' Password Gen")
    x = 0
    cd = ['/','*','.',',','#',1,2,3,4,5,6,7,8,9,0,"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P",'Q','R','S','T','U','V','W','X','Y','Z']
    d = int(input("Elige la cantidad de digitos de tu contraseña"))
    print("")
    print("Digitos elegidos:",d)
    time.sleep(0.5)
    print("")
    print('procesando...')
    time.sleep(3)

    ddc = [random.choice(cd) for _ in range(d)]

    password = ''.join(map(str, ddc))

    print('')
    print("Tu contraseña generada es:", password)
    print('')
    time.sleep(1)
