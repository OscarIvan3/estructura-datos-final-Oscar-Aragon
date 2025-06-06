def isIsomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False  # Si tienen diferente longitud, no pueden ser isomorfas

    mapping_s_t = {}          # Diccionario para mapear caracteres de s -> t
    mapped_characters = set() # Conjunto para registrar caracteres ya usados en t

    for char_s, char_t in zip(s, t):
        if char_s in mapping_s_t:
            # Si ya hay un mapeo, verificar que sea consistente
            if mapping_s_t[char_s] != char_t:
                return False
        else:
            # Si char_t ya fue usado por otro carácter, no es válido
            if char_t in mapped_characters:
                return False
            # Registrar el nuevo mapeo
            mapping_s_t[char_s] = char_t
            mapped_characters.add(char_t)

    return True  # Si pasa todo, son isomorfas

# Ejemplos de prueba
print(isIsomorphic("egg", "add"))     # True
print(isIsomorphic("foo", "bar"))     # False
print(isIsomorphic("paper", "title")) # True
