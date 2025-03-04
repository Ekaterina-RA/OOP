from src.product import Product


def test_product_creation():
    product_info = {"name": "Смартфон", "price": 8000, "description": "Современный смартфон", "rest": 20}
    product = Product.new_product(product_info)
    assert isinstance(product, Product), "Объект не является экземпляром Product"
    assert product.name == "Смартфон", "Ошибка в имени продукта"
    assert product.price == 8000, "Ошибка в цене продукта"
    assert product.description == "Современный смартфон", "Ошибка в описании продукта"
    assert product.rest == 20, "Ошибка в количестве на складе"


def test_price_getter():
    product_info = {"name": "Смартфон", "price": 8000, "description": "Современный смартфон", "rest": 20}
    product = Product.new_product(product_info)
    assert product.price == 8000, "Геттер цены работает некорректно"


def test_price_setter_valid():
    product_info = {"name": "Смартфон", "price": 8000, "description": "Современный смартфон", "rest": 20}
    product = Product.new_product(product_info)
    product.price = 9000
    assert product.price == 9000, "Сеттер цены не работает корректно с положительным значением"


def test_price_setter_invalid(capsys):
    product_info = {"name": "Смартфон", "price": 8000, "description": "Современный смартфон", "rest": 20}
    product = Product.new_product(product_info)
    product.price = -500  # Установим отрицательную цену

    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out


def test_list_of_products_method():
    product_info = {"name": "Смартфон", "price": 8000, "description": "Современный смартфон", "rest": 20}
    product = Product.new_product(product_info)
    expected_output = "Смартфон, 8000 руб. Остаток: 20 шт."
    assert (
        product.__list_of_products__() == expected_output
    ), "Метод __list_of_products__ не возвращает ожидаемый результат"
