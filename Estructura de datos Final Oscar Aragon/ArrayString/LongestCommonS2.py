def longest_common_prefix_alt(strs):
    if not strs:
        return ""

    for i in range(len(strs[0])):  # Recorremos por carácter
        char = strs[0][i]
        for s in strs[1:]:
            if i >= len(s) or s[i] != char:
                return strs[0][:i]  # Retorna hasta donde coincidan
    return strs[0]

# Pruebas
print("Output:", longest_common_prefix_alt(["flower", "flow", "flight"]))  # "fl"
print("Output:", longest_common_prefix_alt(["dog", "racecar", "car"]))     # ""
