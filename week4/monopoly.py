# 1. Name:
#      Nefi Melgar
# 2. Assignment Name:
#      Lab 04: Monopoly
# 3. Assignment Description:
#      The purpose of the program is to inform the user if he or she is able
#      to build a hotel on Pennsylvania Avenue
# 4. What was the hardest part? Be as specific as possible.
#      I had different issues. Despite of having the flowchart, it was a little harder
#      to correctly organize the code to match the design.
#      It took me a good amount of time to think in the most efficient solution
#      while using my current skills, I'm not sure if using just if/elses was the best
#      solution, maybe using jump tables would be more efficient due of the amount of
#      possible scenarios. I tried to avoid repeating as much code as I can, but at many
#      parts it was not possible because of the different possibilities.
#      I tried to reduce the amount of questions for the user to easily reach the purpose
#      of the program.
#      It seems that I wasn't really able to check the test cases as the specifications said
#      because my design isn't the same, that's why I had a hard time while testing it, I tried
#      to test it as the instructions said but adapted to the variations I did. The expected
#      results are reached so, I don't know if that's right or wrong. 
# 5. How long did it take for you to complete the assignment?
#      It took me around 6 hours to complete the reading and the assignment.

out_no_properties = "You cannot purchase a hotel until you own all the properties of a given color group."
out_no_cash = "You do not have sufficient funds to purchase a hotel at this time."
out_no_houses_avaiable = "There are not enough houses available for purchase at this time."
out_no_hotels_available = "There are not enough hotels available for purchase at this time."
out_already_has_hotel = "You cannot purchase a hotel if the property already has one."
out_unavailable = "That option is not available"
out_swap_correct = "You can swap"
out_swap_error = "Not able to swap."
purchase_options = {"A": "This will cost $[price]. \nPurchase 1 hotel and [number of houses] house(s). \nPut 1 hotel on Pennsylvania and return any houses to the bank. \nPut [number of houses] house(s) on North Carolina. \nPut [number of houses] house(s) on Pacific.",
                    "B": "This will cost $[price].\nPurchase 1 hotel and [number of houses] house(s).\nPut 1 hotel on Pennsylvania and return any houses to the bank.\nPut [number of houses] house(s) on North Carolina.",
                    "C": "This will cost $[price].\nPurchase 1 hotel and [number of houses] house(s).\nPut 1 hotel on Pennsylvania and return any houses to the bank.\nPut [number of houses] house(s) on Pacific.",
                    "D": "This will cost $[price].\nPurchase 1 hotel and [number of houses] house(s).\nPut 1 hotel on Pennsylvania and return any houses to the bank."}


def swap_check():
    """Function that will check if the swap option is available or not"""
    hotel_at_property = input(
        "\nDoes the property have an hotel? (Y/N) ")
    if hotel_at_property.upper() == "Y":
        print(f"{out_swap_correct} with {swap_option}'s 4 houses.")
    elif hotel_at_property.upper() == "N":
        print(out_swap_error)
    else:
        print(out_unavailable)


# 1. PROGRAM STARTS HERE
green_properties = input("Do you own all the green properties? (Y/N) ")

if green_properties.upper() == "Y":

    four_houses = input("\nDo all your green properties have 4 houses? (Y/N) ")
    if four_houses.upper() == "Y":
        swap = input("\nDo you wanna swap? (Y/N) ")

        # USER WANTS TO SWAP
        if swap.upper() == "Y":
            swap_option = input(
                "\nDo you want to swap with NC or PC? (NC/PC) ")
            if swap_option.upper() == "NC":
                swap_check()
            elif swap_option.upper() == "PC":
                swap_check()
            else:
                print(out_unavailable)

        # USER DOESNT WANT TO SWAP
        elif swap.upper() == "N":
            hotel_at_property = input(
                "\nDoes the property have an hotel? (Y/N) ")
            if hotel_at_property.upper() == "Y":
                print(out_already_has_hotel)
            elif hotel_at_property.upper() == "N":
                cash_to_spend = int(
                    input("\nHow much cash you have to spend? $"))

                # check available cash
                if cash_to_spend < 200:
                    print(out_no_cash)
                else:
                    # check available hotels
                    available_hotels = int(
                        input("\nHow many hotels are there to purchase? "))
                    if available_hotels == 0:
                        print(out_no_hotels_available)
                    else:
                        print("\nHere's your purchase option: ")
                        for option, description in purchase_options.items():
                            if option == "D":
                                print(
                                    f"Option {option}. Description: {description}\n")
                            else:
                                pass
            else:
                print(out_unavailable)
        else:
            print(out_unavailable)

            #
            #
            #
            # IF USER DOESNT HAVE 4 HOUSES IN ALL THE GREEN PROPERTIES
    else:
        # check available cash
        cash_to_spend = int(input("\nHow much cash you have to spend? $"))
        if cash_to_spend < 200:
            print(out_no_cash)
        else:
            # check available houses
            available_houses = int(
                input("\nHow many houses are there to purchase? "))
            if available_houses == 0:
                print(out_no_houses_avaiable)
            else:
                # check available hotels
                available_hotels = int(
                    input("\nHow many hotels are there to purchase? "))
                if available_hotels == 0:
                    print(out_no_hotels_available)
                else:
                    # print purchase options
                    for option, description in purchase_options.items():
                        if option != "D":
                            print(
                                f"Option {option}. Description: {description}\n")
                        else:
                            print("No option available")
                    purchase_needs = input(
                        "\nWhat option is better for you? ")

                    if purchase_needs.upper() == "A" or purchase_needs.upper() == "B" or purchase_needs.upper() == "C":
                        print("Thanks for your purchase.")
                    else:
                        print("Purchase not available.")


else:
    print(out_no_properties)
