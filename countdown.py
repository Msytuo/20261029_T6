"""
"""
import time
import random

file = open("colores.txt", "r")
contenido = file.read()
#print(contenido)

file.close()

colores = contenido.split(",")

#print(colores)

cables_salvar = random.choice(colores)
colores.remove(cables_salvar)

cables_explotar = random.choice(colores)



for number in range(10,-1,-1):
    
    if number == 6:

        print("...")
        
    if number < 8 and number > 2:
        continue
    print(number)
    time.sleep(1)
    if number == 8: 
        print("Che podes para la bomba y salvar la pileta, hay unos cable prueba a cortar uno.")
        cable = input("¿Que cable cortamos? (azul,verde,rojo): ").lower()
        if cable == cables_explotar:
            print("BOOM, conshe tu madre!!!")
            print(f"NAAA SOS UN BOLUDO EL {cables_salvar} ERA EL BUENO")
            break
        elif cable == cables_salvar:
            print("Mi causita desactivaste la bomba weon, vayapos a por un cui.")
            break

        else: 
            print("ESE CABLE NO VALE PARA NADA BOLUDO, LA BOMBA VA A EXPLOTAR LA PILETA.")
    
    if number == 0:
        print("BOOM, conshe tu madre!!!")
        print("NAAA EL PIPITA HIGUAN ERA MAS RAPIDO QUE VOS")
        