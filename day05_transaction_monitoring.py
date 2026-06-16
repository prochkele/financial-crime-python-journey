country = input("Country: ")
amount = int(input("Transaction amount: "))

if amount > 10000:
    print("Investigate Immediately")
elif amount > 5000:
    print("Review Required")
else:
    print("Normal Transaction")

if country == "Russia":
    print("High Risk Country")
elif country == "Iran":
    print("High Risk Country")
