# Explicado el programa:
# Esta clase determina si un número es "feliz".
# Un número feliz es aquel que al reemplazarlo repetidamente por la suma de los cuadrados de sus dígitos, eventualmente llega a 1.
# Si entra en un ciclo que no incluye el 1, no es feliz.

class HappyNumber:
    @staticmethod
    def is_happy(n: int) -> bool:
        seen_numbers = set()

        while n != 1 and n not in seen_numbers:
            seen_numbers.add(n)
            n = HappyNumber.sum_of_squares(n)

        return n == 1

    @staticmethod
    def sum_of_squares(n: int) -> int:
        total = 0
        while n > 0:
            digit = n % 10
            total += digit * digit
            n //= 10
        return total

# Pruebas
print(HappyNumber.is_happy(19))  # True
print(HappyNumber.is_happy(2))   # False
