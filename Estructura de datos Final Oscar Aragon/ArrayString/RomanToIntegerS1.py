def roman_to_int(s: str) -> int:
    # Mapa de valores romanos
    roman_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    total = 0
    prev_value = 0

    # Recorremos de derecha a izquierda
    for char in reversed(s):
        current_value = roman_map[char]
        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value
        prev_value = current_value

    return total

# Pruebas
print(roman_to_int("III"))      # 3
print(roman_to_int("LVIII"))    # 58
print(roman_to_int("MCMXCIV"))  # 1994