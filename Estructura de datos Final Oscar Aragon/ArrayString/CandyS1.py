def candy(ratings):
    n = len(ratings)
    candies = [1] * n  # Todos empiezan con 1 caramelo

    # Paso 1: Izquierda a derecha
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1

    # Paso 2: Derecha a izquierda
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)

    return sum(candies)
