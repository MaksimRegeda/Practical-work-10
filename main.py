# Задача 10.1.

def fast_power(a, n):
    if n == 0:
        return 1

    half = fast_power(a, n // 2)

    if n % 2 == 0:
        return half * half

    else:
        return a * half * half


a = 2
n = 8

result = fast_power(a, n)

print("Число:", a)
print("Степінь:", n)
print("Результат:", result)

# Задача 10.2.

def generate_brackets(n):
    result = []

    def backtrack(current, opened, closed):
        if len(current) == 2 * n:
            result.append(current)
            return

        if opened < n:
            backtrack(
                current + "(",
                opened + 1,
                closed
            )

        if closed < opened:
            backtrack(
                current + ")",
                opened,
                closed + 1
            )

    backtrack("", 0, 0)

    return result

n = 3

sequences = generate_brackets(n)

print("Кількість пар дужок:", n)
print("Правильні послідовності:")

for sequence in sequences:
    print(sequence)

print("Всього:", len(sequences))
