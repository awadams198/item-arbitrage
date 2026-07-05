# ======================================
# Functions
# ======================================

def calculate_profit(item):
    fee_amount = item["expected_sale_price"] * item["fee_rate"]

    gross_profit = item["expected_sale_price"] - item["buy_price"]

    net_profit = (
        item["expected_sale_price"]
        - item["buy_price"]
        - item["shipping_cost"]
        - fee_amount
    )

    return gross_profit, fee_amount, net_profit


def get_decision(net_profit, target_profit):
    if net_profit >= target_profit:
        return "BUY"

    return "PASS"


# ======================================
# Item Information
# ======================================

item = {
    "title": "Animal Crossing: New Leaf",
    "category": "Video Game",
    "subcategory": "Nintendo 3DS",
    "condition": "Loose",

    "buy_price": 10.00,
    "target_profit": 8.00,
    "expected_sale_price": 24.99,
    "shipping_cost": 5.00,
    "fee_rate": 0.1325
}


# ======================================
# Calculated Values
# ======================================

gross_profit, fee_amount, net_profit = calculate_profit(item)

decision = get_decision(
    net_profit,
    item["target_profit"]
)


# ======================================
# Output
# ======================================

print("========== Item Arbitrage CLI ==========\n")

print(f"Item: {item['title']}")
print(f"Category: {item['category']}")
print(f"Subcategory: {item['subcategory']}")
print(f"Condition: {item['condition']}\n")

print(f"Buy Price:          ${item['buy_price']:.2f}")
print(f"Target Profit:      ${item['target_profit']:.2f}")
print(f"Expected Sale:      ${item['expected_sale_price']:.2f}")
print(f"Shipping Cost:      ${item['shipping_cost']:.2f}")
print(f"Fee:                ${fee_amount:.2f}")
print(f"Gross Profit:       ${gross_profit:.2f}")
print(f"Net Profit:         ${net_profit:.2f}")

print(f"\nDecision: {decision}")