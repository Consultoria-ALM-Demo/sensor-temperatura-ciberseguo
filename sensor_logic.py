import hashlib

def verificar_seguridad(dato, firma_recibida):
    llave_secreta = "VALVULINA_SAFE_2026"
    # Concatenamos y limpiamos posibles espacios accidentales
    cadena_a_validar = (str(dato) + llave_secreta).strip()
    hash_esperado = hashlib.sha256(cadena_a_validar.encode()).hexdigest()
    
    if firma_recibida.strip() == hash_esperado:
        print(f"RESULTADO: INTEGRIDAD CONFIRMADA para dato {dato}.")
        return True
    else:
        # Imprimimos el hash que el sistema espera para que puedas verlo en la terminal
        print(f"DEBUG - Hash esperado: {hash_esperado}")
        print(f"RESULTADO: ¡ALERTA DE SEGURIDAD! Firma inválida detectada.")
        return False

if __name__ == "__main__":
    print("--- INICIANDO TEST DE INTEGRIDAD ---")
    
    # Escenario 1: Datos legitimos
    # Usamos el hash exacto que tu sistema ha generado en el paso anterior
    print("\n[Escenario 1: Datos legitimos]")
    h_confirmado = "358b0584bf0e75358944c83ddf7e6247c0acaaef5f79a5391f1806a4c4b1e7ed"
    verificar_seguridad(75, h_confirmado)
    
    # Escenario 2: Intento de Sabotaje
    print("\n[Escenario 2: Intento de Sabotaje]")
    verificar_seguridad(75, "FIRMA_SABOTEADA_999")
# Fin del archivo.