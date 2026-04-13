import hashlib

def verificar_seguridad(dato, firma_recibida):
    # Simulamos una validación de integridad SHA-256 (Mitigación BIEMH26-671)
    llave_secreta = "VALVULINA_SAFE_2026"
    hash_esperado = hashlib.sha256((str(dato) + llave_secreta).encode()).hexdigest()
    
    if firma_recibida == hash_esperado:
        print("Integridad confirmada: El dato es auténtico.")
        return True
    else:
        print("¡ALERTA DE SEGURIDAD! Intento de inyección de datos detectado.")
        return False
# Fin del archivo.
# Modificación de estado para la task. Commit "Implementación de firma SHA-256. Refs BIEMH26-675 status:done"