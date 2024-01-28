class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


def get_cart_total(products, quantities):
    total = 0
    for product, quantity in zip(products, quantities):
        total += product.price * quantity
    return total


def calculate_discount(products, quantities, cart_total):
    rules = {
        "flat_10_discount": 10 if cart_total > 200 else 0,
        "bulk_5_discount": int(0.05 * cart_total) if max(quantities) > 10 else 0,
        "bulk_10_discount": int(0.1 * cart_total) if sum(quantities) > 20 else 0,
        "tiered_50_discount": sum(
            int(0.5 * product.price * (quantity - 15))
            for product, quantity in zip(products, quantities)
            if sum(quantities) > 30 and quantity > 15
        ),
    }

    max_discount = max(rules.values())
    for rule, discount in rules.items():
        if discount == max_discount:
            return rule, discount

    return None, 0


def calculate_fees(products, quantities, gifts):
    total_quantity = sum(quantities)
    shipping_fee = (total_quantity // 10 + (total_quantity % 10 > 0)) * 5
    gift_wrap_fee = sum(5 for is_gift, quantity in zip(gifts, quantities) if is_gift)
    return shipping_fee, gift_wrap_fee


def main():
    products = [
        Product("Product A", 20),
        Product("Product B", 40),
        Product("Product C", 50),
    ]

    quantities = [int(input(f"Enter quantity for {product.name}: ")) for product in products]
    gifts = [input(f"Is {product.name} wrapped as a gift? (yes/no): ").lower() == "yes" for product in products]

    print("\nYour Order:")
    for product, quantity, gift in zip(products, quantities, gifts):
        print(f"{product.name}: Quantity: {quantity}, Is {product.name} wrapped as a gift? ({'yes' if gift else 'no'})")

    cart_total = get_cart_total(products, quantities)
    discount_rule, discount_amount = calculate_discount(products, quantities, cart_total)
    shipping_fee, gift_wrap_fee = calculate_fees(products, quantities, gifts)

    print("\nOrder Details:")
    for product, quantity in zip(products, quantities):
        total_amount = product.price * quantity
        print(
            f"{product.name}: Quantity: {quantity}, Total Amount: ${total_amount}"
        )

    print("\nSubtotal: $", cart_total)
    print(f"Discount Applied: {discount_rule} - Discount Amount: ${discount_amount}")
    print("Shipping Fee: $", shipping_fee, " & Gift wrap fee: $", gift_wrap_fee)
    total = cart_total - discount_amount + shipping_fee + gift_wrap_fee
    print("Total: $", total)


if __name__ == "__main__":
    main()
