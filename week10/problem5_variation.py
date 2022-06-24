account_balances = [10, 1, -1, -1]

total = 0
for amount in account_balances:
    total += amount

print(f"Total net worth is: ${total}")

# with the single function
def net_worth(account_balance):
    total = 0
    for amount in account_balances:
        total += amount

    return total
