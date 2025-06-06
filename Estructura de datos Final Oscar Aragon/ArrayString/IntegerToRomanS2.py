def int_to_roman_by_place(num: int) -> str:
    # Paso 1: Listas de representación fija por posición
    thousands = ["", "M", "MM", "MMM"]
    hundreds  = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    tens      = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    ones      = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

    # Paso 2: Componer según cada dígito del número
    return (
        thousands[num // 1000] +
        hundreds[(num % 1000) // 100] +
        tens[(num % 100) // 10] +
        ones[num % 10]
    )