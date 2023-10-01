def calculate_total(cart):
    """Calculates the total price of items in the cart."""
    total = 0
    for item in cart:
        total += item['price']
    return total


def display_total(total):
    """Displays the total price."""
    print(f"Total price: ${total:.2f}")


CART = [
    {'name': 'Item A', 'price': 10.99},
    {'name': 'Item B', 'price': 5.99},
    {'name': 'Item C', 'price': 8.49}
]

for item in CART:
    print(f"Item: {item['name']} - Price: ${item['price']:.2f}")

shopping_cart_total = calculate_total(CART)
display_total(shopping_cart_total)
