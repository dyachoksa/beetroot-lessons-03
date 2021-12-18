def calculate_tax_amount(amount, tax_percent=10):
    """Calculates tax amount from amount based on tax percentage (in form 10%)"""
    if tax_percent is None:
        raise ValueError("Tax percent can't be None")

    if tax_percent < 0:
        raise ValueError("Tax percent can't be negative")

    return amount * (tax_percent/100)


def main():
    amount = float(input("Please enter your income amount: "))
    tax_amount = calculate_tax_amount(amount)

    print("You need to pay: {:.2f}".format(tax_amount))


if __name__ == "__main__":
    main()
