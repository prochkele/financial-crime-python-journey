amount = int(input("Transaction amount: "))
country = input("Country: ")

if amount > 10000 and country == "Russia":
    print("AML Alert")

elif amount > 5000:
    print("Review Required")

else:
    print("Normal Transaction")
