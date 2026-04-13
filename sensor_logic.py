import hashlib

def verificar_seguridad(dato, firma_recibida):
    # La clave secreta debe coincidir con la usada para generar el hash de la Iteración 1
    llave_secreta = "VALVULINA_SAFE_2026"
    
    # Generamos el hash de integridad
    hash_esperado = hashlib.sha256((str(dato) + llave_secreta).encode()).hexdigest()
    
    if firma_recibida == hash_esperado:
        print(f"RESULTADO: INTEGRIDAD CONFIRMADA para dato {dato}.")
        return True
    else:
        print(f"RESULTADO: ¡ALERTA DE SEGURIDAD! Firma inválida detectada.")
        return False

# Ejemplo de uso para demo:
# Si ejecutas: verificar_seguridad(75, "59837508...") -> Dirá INTEGRIDAD CONFIRMADA
# Si ejecutas: verificar_seguridad(75, "FIRMA_SABOTEADA_999") -> Dirá ALERTA DE SEGURIDAD
# Fin del archivo.