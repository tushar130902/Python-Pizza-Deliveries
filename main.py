print("Welcome To Python Pizza Deliveries")

size = input("What Size Pizza Do You want? S, M OR L :")

pepporoni = input("Do You Want Pepporoni on your Pizza ? Y OR N :")

extra_cheesse = input("Do You Want Extra Cheese ? Y OR N :")

bill = 0

if size == "S" :
    bill += 15
elif size == "M":
    bill += 20
elif size == "L" :
    bill += 25
else:
    print("You Choose Wrong Keyword ")

if pepporoni == "y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheesse == "y":
    bill += 1

# print(f"Your total bill is ₹{bill}.")
print("your total bill is ₹ ", bill)