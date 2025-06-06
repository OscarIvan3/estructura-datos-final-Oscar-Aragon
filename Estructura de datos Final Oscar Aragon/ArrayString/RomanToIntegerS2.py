def roman_to_int_alt(s: str) -> int:
    roman_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    total = 0
    i = 0
    while i < len(s):
        # Si hay un siguiente carácter y su valor es mayor, es una resta especial
        if i + 1 < len(s) and roman_map[s[i]] < roman_map[s[i + 1]]:
            total += roman_map[s[i + 1]] - roman_map[s[i]]
            i += 2  # Saltamos ambos caracteres
        else:
            total += roman_map[s[i]]
            i += 1
    return total

# Pruebas
print(roman_to_int_alt("III"))      # 3
print(roman_to_int_alt("LVIII"))    # 58
print(roman_to_int_alt("MCMXCIV"))  # 1994