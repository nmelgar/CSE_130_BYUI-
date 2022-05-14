purchase_options = {"A": "This will cost $[price]. \nPurchase 1 hotel and [number of houses] house(s). \nPut 1 hotel on Pennsylvania and return any houses to the bank. \nPut [number of houses] house(s) on North Carolina. \nPut [number of houses] house(s) on Pacific.",
                    "B": "This will cost $[price].\nPurchase 1 hotel and [number of houses] house(s).\nPut 1 hotel on Pennsylvania and return any houses to the bank.\nPut [number of houses] house(s) on North Carolina.",
                    "C": "This will cost $[price].\nPurchase 1 hotel and [number of houses] house(s).\nPut 1 hotel on Pennsylvania and return any houses to the bank.\nPut [number of houses] house(s) on Pacific.",
                    "D": "This will cost $[price].\nPurchase 1 hotel and [number of houses] house(s).\nPut 1 hotel on Pennsylvania and return any houses to the bank."}


for option, description in purchase_options.items():
    if option != "D":
        print(
            f"Option {option}. Description: {description}\n")
    else:
        print(" ")
purchase_needs = input(
    "What option is better for you? ")
if purchase_needs.upper() == "A" or purchase_needs.upper() == "B" or purchase_needs.upper() == "C":
    print("Thanks for your purchase.")
else:
    print("Purchase not available.")
