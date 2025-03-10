import pytest

from src.category import Category
from src.list_of_products import LawnGrass, Smartphone
from src.product import Product


def test_category_creation():
    category = Category("Смартфоны")
    assert category.name == "Смартфоны"
    assert category.products == ""


def test_category_add_product():
    category = Category("Смартфоны")
    smartphone = Smartphone("iPhone 12", 80000, 10, 90, "iPhone 12", 128, "Red")
    category.add_product(smartphone)
    assert len(category._Category__products) == 1
    assert category.products == str(smartphone)


def test_category_add_invalid_product():
    category = Category("Тестовая категория")
    with pytest.raises(TypeError):
        category.add_product("Не продукт")


def test_category_product_count():
    category = Category("Тестовая категория")
    product1 = Product("Товар 1", 100.0, 5)
    product2 = LawnGrass("Газонная Трава", 1500.0, 10, "Россия", 7, "Зеленый")

    category.add_product(product1)
    category.add_product(product2)

    assert category.__str__() == "Тестовая категория, количество продуктов: 15 шт."
