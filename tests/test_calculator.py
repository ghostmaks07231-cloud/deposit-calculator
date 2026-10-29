import pytest
from calculator import calculate_deposit_income

# Тест 1: Проверка стандартного расчета
def test_normal_calculation():
    # 100000 руб под 10% на 365 дней = 10000 руб
    assert calculate_deposit_income(100000, 10, 365) == 10000.0

# Тест 2: Проверка расчета с дробными значениями
def test_fractional_calculation():
    # Округление до 2 знаков
    assert calculate_deposit_income(50000, 7.5, 100) == 1027.4

# Тест 3: Проверка обработки нулевых/отрицательных значений
def test_invalid_values():
    with pytest.raises(ValueError, match="Все значения должны быть больше нуля"):
        calculate_deposit_income(0, 10, 365)
        
    with pytest.raises(ValueError):
        calculate_deposit_income(10000, -5, 30)