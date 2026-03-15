def save_price_check(item: dict) -> bool:
    """
    Перевіряє ціну на безпечність та поріг у 1000.
    """

    try:
        price = float(item.get("price", 0))
        return price > 1000
    except (ValueError, TypeError):
        return False