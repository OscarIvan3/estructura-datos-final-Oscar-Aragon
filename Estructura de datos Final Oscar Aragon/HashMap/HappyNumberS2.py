def isHappy(n: int) -> bool:
    # Función auxiliar que calcula la suma de los cuadrados de los dígitos de un número
    def get_next(number):
        total_sum = 0
        while number > 0:
            digit = number % 10          # Obtiene el último dígito
            total_sum += digit ** 2      # Suma el cuadrado del dígito
            number //= 10                # Elimina el último dígito
        return total_sum

    seen = set()  # Conjunto para guardar los números ya vistos y detectar ciclos
    
    # Repite el proceso hasta que el número sea 1 (es feliz) o entre en un ciclo
    while n != 1 and n not in seen:
        seen.add(n)         # Guarda el número actual para detectar ciclos
        n = get_next(n)     # Reemplaza el número por la suma de los cuadrados de sus dígitos
    
    return n == 1           # Devuelve True si es feliz, False si entra en un ciclo

# Ejemplos de uso
print(isHappy(19))  # Salida: True (es un número feliz)
print(isHappy(2))   # Salida: False (entra en un ciclo)
