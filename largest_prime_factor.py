num = 12
factors = []
for i in range(1, num + 1):
    if num % i == 0:
        factors.append(i)

prime_factors = []
for factor in factors:
    if factor == 1:
        continue
    is_prime = True
    for i in range(2, int(factor ** 0.5) + 1):
        if factor % i == 0:
            is_prime = False
            break
    if is_prime:
        prime_factors.append(factor)

print(prime_factors)