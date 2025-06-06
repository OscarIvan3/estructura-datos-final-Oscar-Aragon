def isAnagram(s: str, t: str) -> bool:
    # Paso 1: Verifica si las longitudes son diferentes
    if len(s) != len(t):
        return False

    # Paso 2: Crea una lista para contar las frecuencias (una posición por cada letra del alfabeto)
    count = [0] * 26  # Solo letras minúsculas del alfabeto inglés

    # Paso 3: Actualiza las frecuencias
    for i in range(len(s)):
        count[ord(s[i]) - ord('a')] += 1
        count[ord(t[i]) - ord('a')] -= 1

    # Paso 4: Verifica si todas las frecuencias son cero
    for freq in count:
        if freq != 0:
            return False

    # Paso 5: Si todo está bien, son anagramas
    return True

# Pruebas
print(isAnagram("anagram", "nagaram"))  # True
print(isAnagram("rat", "car"))          # False
