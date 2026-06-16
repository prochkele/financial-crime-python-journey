country = input("Country: ")
amount = int(input("Transaction amount: "))

if amount > 1000:
    print("High Risk Transaction")
else:
    print("Low Risk Transaction")

if country == "Russia":
    print("Manual Review Required")
