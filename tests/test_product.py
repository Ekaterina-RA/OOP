import pytest

from src.product import Product


def test_creation_info():
    product = Product("Samsung Galaxy S23 Ultra", 180000.0, 5)
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.price == 180000.0
    assert product.rest == 5


def test_repr():
    product = Product("Xiaomi Redmi Note 11", 31000.0, 14)
    assert repr(product) == "Product(name=Xiaomi Redmi Note 11, price=31000.0, rest=14)"


def test_str():
    product = Product("Samsung Galaxy S23 Ultra", 180000.0, 5)
    assert str(product) == "Samsung Galaxy S23 Ultra, 180000.00 руб. Остаток: 5 шт."


def test_addition():
    product_1 = Product("Samsung Galaxy S23 Ultra", 180000.0, 5)
    product_2 = Product("Xiaomi Redmi Note 11", 31000.0, 14)
    expected_total_value = (180000.0 * 5) + (31000.0 * 14)
    assert product_1 + product_2 == expected_total_value


def test_product_creation():
    product_info = {"name": "Смартфон", "price": 8000, "rest": 20}
    product = Product.new_product(product_info)
    assert product.name == "Смартфон"
    assert product.price == 8000.0
    assert product.rest == 20


def test_price_getter():
    product_info = {"name": "Смартфон", "price": 8000, "rest": 20}
    product = Product.new_product(product_info)
    assert product.price == 8000.0, "Геттер цены работает некорректно"


def test_price_setter_valid():
    product_info = {"name": "Смартфон", "price": 8000, "rest": 20}
    product = Product.new_product(product_info)
    product.price = 9000
    assert product.price == 9000.0, "Сеттер цены не работает корректно с положительным значением"  # Сравниваем с float


def test_price_setter_invalid(capsys):
    product_info = {"name": "Смартфон", "price": 8000, "rest": 20}
    product = Product.new_product(product_info)
    product.price = -500  # Установим отрицательную цену

    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out


def test_product_initialization_valid():
    """Тест для корректной инициализации продукта с положительным остатком."""
    product = Product("Samsung Galaxy S23 Ultra", 180000.0, 5)
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.price == 180000.0
    assert product.rest == 5


def test_product_initialization_zero_rest():
    """Тест для случая, когда остаток равен нулю, должен выбрасывать ValueError."""
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Product("Samsung Galaxy S23 Ultra", 180000.0, 0)


def test_product_initialization_negative_rest():
    """Тест для случая, когда остаток отрицательный, должен выбрасывать ValueError."""
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Product("Iphone 15", 210000.0, 0)
