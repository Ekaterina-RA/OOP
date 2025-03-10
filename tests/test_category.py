from src.category import Category
from src.product import Product


def test_add_product():
    category = Category("Смартфон")
    product = Product("Samsung Galaxy S23 Ultra", 180000.0, 5)

    category.add_product(product)
    assert Category.product_count == 1, "Ошибка: Счетчик продуктов должен увеличиться на 1."
    print("test_add_product passed!")


def test_add_invalid_product():
    category = Category("Смартфоны")

    try:
        category.add_product("Некорректный продукт")
    except ValueError as e:
        assert str(e) == "Только объекты класса Product добавляются.", "Ошибка: Неверное сообщение об ошибке."
    else:
        assert False, "Ошибка: Исключение не было вызвано при добавлении некорректного продукта."

    print("test_add_invalid_product passed!")


def test_products_property():
    category = Category("Смартфоны")
    product1 = Product("Смартфон", 180000.0, 5)
    product2 = Product("Телевизор 55 QLED 4K", 123000.0, 7)

    category.add_product(product1)
    category.add_product(product2)

    expected_output = "Смартфон, 180000.0 руб. Остаток: 5 шт.\nТелевизор 55 QLED 4K, 123000.0 руб. Остаток: 7 шт."
    assert category.products == expected_output, "Ошибка: Неверный вывод списка продуктов."

    print("test_products_property passed!")
