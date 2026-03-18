from validators import save_price_check

def get_expensive_items(items: list[dict]) -> list[str]:
    return [item.get('name', 'Unknown Item') for item in items if save_price_check(item)]

data = [
    {"name": "Phone", "price": 10000},
    {"name": "Laptop", "price": "ціна за запитом"},
    {"price": 5000}, # Немає імені
    {"name": "Old Cable", "price": None} # Ціна є, але вона порожня
]

if __name__ == '__main__':
    result = get_expensive_items(data)
    print(f'Знайдено дорогіх товарів: {result}')

