list_1 = 100

for number in range(2, list_1 + 1):
    if number <= list_1:
        not_prime = number * number
    number += 1
    print(not_prime)