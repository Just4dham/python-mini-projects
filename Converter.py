while True:
    currency = input("What currency? (Euro, USD, or KWD): ").strip().upper()

    if currency == "USD":
        num = float(input("Enter the amount: "))

        print(f"SAR: {num * 3.75}")

    elif currency in ["EURO", "EUR"]:

        num = float(input("Enter the amount: "))

        print(f"SAR: {num * 4.33}")
    elif currency == "KWD":

        num = float(input("Enter the amount: "))

        print(f"SAR: {num * 12.15}")

    else:
        print("Enter a valid currency :)")

    Quit = input("Quit? (Y/N): ").strip().upper()
    if Quit == "Y":
        break
