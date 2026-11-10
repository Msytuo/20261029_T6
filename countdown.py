"""
"""
import time



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
        if cable == "rojo":
            print("BOOM, conshe tu madre!!!")
            break
        elif cable == "verde":
            print("Mi causita desactivaste la bomba weon, vayapos a por un cui.")
            break
        elif cable == "azul":
            print("Aaaa culiao no hace nada la bomba sigue.")

        else: 
            print("NO HAS CORTADO NADA BOLUDO, LA BOMBA VA A EXPLOTAR LA PILETA.")
    
    if number == 0:
        print("BOOM, conshe tu madre!!!")
