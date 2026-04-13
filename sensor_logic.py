# Sistema de Control de Temperatura Industrial
# ID de Referencia: TEMP-01, TEMP-02

import time

def leer_sensor():
    # Simulación de lectura de temperatura
    return 105 

def verificar_seguridad(valor):
    # Lógica de ciberseguridad para evitar manipulaciones (TEMP-02)
    print("Verificando firma digital del dato...")
    return True

def bucle_principal():
    temp = leer_sensor()
    if verificar_seguridad(temp):
        if temp > 100:
            print(f"ALERTA: Temperatura crítica de {temp}C detectada!")
        else:
            print("Temperatura normal.")

if __name__ == "__main__":
    bucle_principal()
# Fin del archivo.