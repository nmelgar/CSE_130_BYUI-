n = 20
assert n > 1, "N must be greater than 1"

check_range = range(2, n + 1)

not_prime_list = []
prime_list = []

for number in check_range:
    for number in range(number*number, n+1, number):
        if number not in not_prime_list:
            not_prime_list.append(number)
for number in check_range:
    if number not in not_prime_list and number not in prime_list:
        prime_list.append(number)

assert len(prime_list) > 0, "List cannot be empty"
print(prime_list)
# print(not_prime_list)