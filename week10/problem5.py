
def main():
    # call the accounts
    balances = accounts()

    # call the function to get the total
    total = net_worth(balances)

    # print the total
    print(f"Total net worth is ${total}.")


def accounts():
    """Function that holds the amounts for the different
    accounts of the user"""
    # add or delete amounts as needed
    account_balances = {
        "savings": [1, 1, 1, 1],
        "investment": [1, 1, 1],
        "mortgage": [-1, -1, -1],
        "credit_card": [-1, -1, -1],
        "car_loan": [-1, -1, -1]
    }

    return account_balances


def net_worth(account_balances):
    """This function will add the total of each account
    to the net worth of the user.
    """
    total = 0
    for key, value in account_balances.items():
        savings = account_balances['savings']
        investment = account_balances['investment']
        mortgage = account_balances['mortgage']
        credit_card = account_balances['credit_card']
        car_loan = account_balances['car_loan']

        if key == "savings":
            for number in savings:
                total += number

        elif key == "investment":
            for invested_amount in investment:
                total += invested_amount

        elif key == "mortgage":
            for mortgage_amount in mortgage:
                total += mortgage_amount

        elif key == "credit_card":
            for card_payment in credit_card:
                total += card_payment

        elif key == 'car_loan':
            for car_payment in car_loan:
                total += car_payment

    return total


if __name__ == "__main__":
    main()


# total = 0
# total_savings = 0
# total_investment = 0
# total_mortgage = 0

# for key, value in account_balances.items():
#     savings = account_balances['savings']
#     if key == "savings":
#         for number in savings:
#             total_savings += number

#     investment = account_balances['investment']
#     if key == "investment":
#         for invested_amount in investment:
#             total_investment += invested_amount

#     mortgage = account_balances['mortgage']
#     if key == "mortgage":
#         for mortgage_amount in mortgage:
#             total_mortgage += mortgage_amount

# total = total_savings + total_investment + total_mortgage

# print(f"total is {total}")
