import heapq

def candy_heap(ratings):
    n = len(ratings)
    candies = [1] * n
    min_heap = [(r, i) for i, r in enumerate(ratings)]
    heapq.heapify(min_heap)

    while min_heap:
        r, i = heapq.heappop(min_heap)

        # Comparar con el vecino izquierdo
        if i > 0 and ratings[i] > ratings[i - 1]:
            candies[i] = max(candies[i], candies[i - 1] + 1)

        # Comparar con el vecino derecho
        if i < n - 1 and ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)

    return sum(candies)