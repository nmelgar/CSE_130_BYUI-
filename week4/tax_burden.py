income = 0

def computeTax(income):
    if income < 123700:
        # 10% tax backet
        #0% 358,607,16
        # 10% 27,400,094
        if income >= 0 and income < 15100:
            if income == 0:
                print("Your tax is 0%")
            else:
                tax = income * 0.10
                print("Your tax is 10%")

        # 15% tax backet
        # 42,195,123
        elif income >= 15100 and income < 61300:
            tax = 1510 + 0.15 * (income - 15100)
            print("Your tax is 15%")

        # 25% tax bracket
        # 24,003,141
        elif income >= 61300:
            tax = 8440 + 0.25 * (income - 61300)
            print("Your tax is 25%")

    elif income >= 123700:
        # 28% tax bracket
        # 4,603,602
        if income < 188450:
            tax = 24040 + 0.28 * (income - 123700)
            print("Your tax is 28%")

        # 33% tax bracket
        # 1,768,562
        elif income >= 188450 and income < 336550:
            tax = 42170 + 0.33 * (income - 188450)
            print("Your tax is 33%")

        # 35% tax bracket
        # 1,245,124
        elif income >= 336550:
            tax = 91043 + 0.35 * (income - 336550)
            print("Your tax is 35%")


computeTax(income)
