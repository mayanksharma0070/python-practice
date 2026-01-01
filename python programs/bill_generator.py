# Grocery Bill Calculator using List

items = ["Rice", "Sugar", "Salt", "Oil", "Milk"]
prices = [60, 40, 20, 120, 50]

print("----- Welcome to Grocery Store -----")
print("Available Items:")
for i in range(len(items)):
    print(f"{i+1}. {items[i]} - Rs.{prices[i]}/kg or litre")

cart = []
quantities = []

n = int(input("Enter how many different items you want to buy: "))

for i in range(n):
    item_no = int(input(f"Enter item number (1-{len(items)}): "))
    qty = float(input(f"Enter quantity (in kg or litre) for {items[item_no-1]}: "))
    cart.append(item_no - 1)
    quantities.append(qty)

total = 0
print("\n----- Your Bill -----")
for i in range(len(cart)):
    index = cart[i]
    cost = prices[index] * quantities[i]
    total += cost
    print(f"{items[index]} - {quantities[i]} kg/litre x Rs.{prices[index]} = Rs.{cost}")

print("-----------------------------")
print(f"Total Bill Amount = Rs.{total}")
print("Thank you! Visit again :)")
