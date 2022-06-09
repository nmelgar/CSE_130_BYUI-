def compute_tax(income):
    tax = -1.0

    #Assert to review that the income should be 0 or a positive number
    assert income > -1, "Income should be 0 or a positive number"

    if income >= 0 and income < 15100:
        tax = income * 0.10
    elif income >= 15100 and income < 61300:
        tax = 1510 + 0.15 * (income - 15100)
    elif income >= 61300 and income < 123700:
        tax = 8440 + 0.25 * (income - 61300)
    elif income >= 123700 and income < 188450:
        tax = 24040 + 0.28 * (income - 123700)
    elif income >= 188450 and income < 336550:
        tax = 42170 + 0.33 * (income - 188450)
    elif income >= 336550:
        tax = (91043 + 0.35) * (income - 336550)
    return tax

# print(compute_tax(-2))