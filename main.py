import random
defensor = {
    "nombre": "Miguel",
    "estatura": 80,          # Su alcance físico base
    "capacidad_salto": 15,   # Lo que se eleva usando los músculos
    "velocidad": 60,
    "resistencia": 30        # Lo dejamos cansado para la prueba
}

delantero = {
    "nombre": "Carlos",
    "estatura": 65,
    "capacidad_salto": 25,   # Este salta más, compensa su estatura
    "velocidad": 85,
    "resistencia": 100       # Fresco
}

def simular_centro():
    # 1. El cansancio afecta ÚNICAMENTE a la capacidad de salto
    factor_defensa = defensor["resistencia"] / 100
    factor_delantero = delantero["resistencia"] / 100
    
    salto_real_defensa = defensor["capacidad_salto"] * factor_defensa
    salto_real_delantero = delantero["capacidad_salto"] * factor_delantero
    
    # 2. El alcance aéreo total es: Estatura + Salto Cansado
    alcance_defensa = defensor["estatura"] + salto_real_defensa
    alcance_delantero = delantero["estatura"] + salto_real_delantero
    
    # 3. Sumamos el factor suerte (Dado del 1 al 10 para balancear)
    suerte_defensa = random.randint(1, 10)
    suerte_delantero = random.randint(1, 10)
    
    poder_final_defensa = alcance_defensa + suerte_defensa
    poder_final_delantero = alcance_delantero + suerte_delantero
    
    # 4. Resultado final de la jugada
    if poder_final_defensa > poder_final_delantero:
        return f"¡Despeje de {defensor['nombre']}! (Poder: {poder_final_defensa:.1f} vs {poder_final_delantero:.1f})"
    else:
        return f"¡Gol de {delantero['nombre']}! (Poder: {poder_final_defensa:.1f} vs {poder_final_delantero:.1f})"   

def simular_pase_al_hueco():
    # 1. El cansancio afecta directamente a la velocidad
    factor_defensa = defensor["resistencia"] / 100
    factor_delantero = delantero["resistencia"] / 100
    
    # Calculamos la velocidad real en este minuto del partido
    velocidad_real_defensa = defensor["velocidad"] * factor_defensa
    velocidad_real_delantero = delantero["velocidad"] * factor_delantero
    
    # 2. Tiramos el dado de la suerte para la carrera (del 1 al 10)
    suerte_defensa = random.randint(1, 10)
    suerte_delantero = random.randint(1, 10)
    
    # 3. El poder de carrera final
    carrera_defensa = velocidad_real_defensa + suerte_defensa
    carrera_delantero = velocidad_real_delantero + suerte_delantero
    
    # 4. Definimos el resultado de la carrera
    if carrera_defensa > carrera_delantero:
        return f"¡Corte providencial! {defensor['nombre']} barrió a tiempo por abajo. (Velocidad: {carrera_defensa:.1f} vs {carrera_delantero:.1f})"
    else:
        return f"¡Mano a mano! {delantero['nombre']} ganó por velocidad y quedó frente al portero. (Velocidad: {carrera_defensa:.1f} vs {carrera_delantero:.1f})"


print("--- JUGADA 1: CENTRO AL ÁREA ---")
print(simular_centro())

print("\n--- JUGADA 2: BALÓN AL HUECO ---")
print(simular_pase_al_hueco())