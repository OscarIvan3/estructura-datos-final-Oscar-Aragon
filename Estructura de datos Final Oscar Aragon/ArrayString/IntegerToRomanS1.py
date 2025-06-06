def int_to_roman_greedy(num: int) -> str:
    # Paso 1: Tabla de valores y símbolos romanos
    values =    [1000, 900, 500, 400, 100, 90,  50, 40, 10, 9,   5,  4,  1]
    symbols = ["M",  "CM", "D", "CD", "C", "XC", "L","XL","X","IX","V","IV","I"]

    # Paso 2: Construir el resultado
    roman = []
    for i in range(len(values)):
        while num >= values[i]:
            roman.append(symbols[i])
            num -= values[i]
    return "".join(roman)
