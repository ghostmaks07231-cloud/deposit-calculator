def calculate_deposit_income(s, p, d):
    """
    Расчёт дохода по вкладу.
    s - сумма вклада
    p - годовая ставка (%)
    d - срок в днях
    """
    if s <= 0 or p <= 0 or d <= 0:
        raise ValueError("Все значения должны быть больше нуля!")
    
    # Формула: Доход = S * P / 100 * D / 365
    income = s * p / 100 * d / 365
    return round(income, 2)