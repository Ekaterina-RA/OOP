from src.product import Product


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


def test_list_of_products_method():
    product_info = {"name": "Смартфон", "price": 8000.0, "rest": 20}
    product = Product.new_product(product_info)
    expected_output = "Смартфон, 8000.0 руб. Остаток: 20 шт."
    assert (
        product.__str__() == expected_output
    ), "Метод __str__ не возвращает ожидаемый результат"  # Теперь используем строковое представление
