def can_complete_circuit(gas, cost):
    total_gas = 0
    total_cost = 0
    tank = 0
    start = 0

    for i in range(len(gas)):
        total_gas += gas[i]
        total_cost += cost[i]
        tank += gas[i] - cost[i]

        # Si el tanque se vacía, significa que no podemos llegar desde 'start' hasta 'i'
        if tank < 0:
            start = i + 1
            tank = 0  # reiniciamos el tanque

    # Si el total de gas es suficiente para cubrir el total de costo, el viaje es posible
    return start if total_gas >= total_cost else -1