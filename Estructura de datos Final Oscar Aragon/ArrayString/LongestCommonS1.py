def longest_common_prefix(strs):
    if not strs:
        return ""

    prefix = strs[0]  # Tomamos la primera cadena como referencia
    for i in range(1, len(strs)):
        # Mientras la cadena actual no empiece con el prefijo
        while not strs[i].startswith(prefix):
            prefix = prefix[:-1]  # Reducimos el prefijo
            if not prefix:
                return ""
    return prefix

# Pruebas
input1 = ["flower", "flow", "flight"]
print("Output:", longest_common_prefix(input1))  # "fl"

input2 = ["dog", "racecar", "car"]
print("Output:", longest_common_prefix(input2))  # ""