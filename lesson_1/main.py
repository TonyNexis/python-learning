from validators import save_price_check

def get_expensive_items(items: list[dict]) -> list[str]:
    return [item.get('name', 'Unknown Item') for item in items if save_price_check(item)]

broken_items = [
    {"name": "Phone", "price": 10000},
    {"name": "Laptop", "price": "ціна за запитом"},
    {"price": 5000}, # Немає імені
    {"name": "Old Cable", "price": None} # Ціна є, але вона порожня
]

print(get_expensive_items(broken_items))