def add_two_numbers_list(l1, l2):
    result = []
    carry = 0
    i, j = 0, 0

    while i < len(l1) or j < len(l2) or carry:
        sum_ = carry

        if i < len(l1):
            sum_ += l1[i]
            i += 1
        if j < len(l2):
            sum_ += l2[j]
            j += 1

        carry = sum_ // 10
        result.append(sum_ % 10)

    return result

