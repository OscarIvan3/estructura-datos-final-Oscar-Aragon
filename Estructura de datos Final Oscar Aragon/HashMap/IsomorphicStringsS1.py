def isIsomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    map_st = {}  # Mapeo de caracteres de s -> t
    map_ts = {}  # Mapeo de caracteres de t -> s

    for char_s, char_t in zip(s, t):
        # Verificar mapeo de s -> t
        if char_s in map_st:
            if map_st[char_s] != char_t:
                return False
        else:
            map_st[char_s] = char_t

        # Verificar mapeo de t -> s
        if char_t in map_ts:
            if map_ts[char_t] != char_s:
                return False
        else:
            map_ts[char_t] = char_s

    return True

# Pruebas
print(isIsomorphic("egg", "add"))     # True
print(isIsomorphic("foo", "bar"))     # False
print(isIsomorphic("paper", "title")) # True
