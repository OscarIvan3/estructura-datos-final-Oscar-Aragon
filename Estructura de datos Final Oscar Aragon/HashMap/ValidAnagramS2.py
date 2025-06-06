from collections import Counter

def isAnagram(s: str, t: str) -> bool:
    # Paso 1: Comparar las frecuencias de los caracteres usando Counter
    return Counter(s) == Counter(t)

# Pruebas
print(isAnagram("anagram", "nagaram"))  # True
print(isAnagram("rat", "car"))          # False