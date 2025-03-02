import pytest

from src.category import Category
from src.product import Product


@pytest.fixture(autouse=True)
def reset_category_count():
    """Сброс статических атрибутов перед каждым тестом."""
    Category.category_count = 0
    Category.product_count = 0


def test_category_initialization():
    """Тестирование корректности инициализации объекта Category"""
    category = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
    )
    assert category.name == "Смартфоны"
    assert (
        category.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert Category.category_count == 1  # Проверяем, что счетчик категорий увеличился


def test_add_product():
    """Тестирование добавления продукта в категорию"""
    category = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
    )
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

    category.add_product(product)

    assert len(category.products) == 1  # Проверяем, что продукт добавлен
    assert category.products[0] == product  # Проверяем, что добавленный продукт правильный
    assert Category.product_count == 1  # Проверяем, что счетчик товаров увеличился


def test_multiple_categories():
    """Тестирование создания нескольких категорий"""
    category1 = Category("Смартфоны", "Категория для смартфонов")
    category2 = Category("Телевизоры", "Для просмотра телепередач")

    assert Category.category_count == 2  # Проверяем, что счетчик категорий увеличился


def test_product_count_in_category():
    """Тестирование подсчета товаров в категории"""
    category = Category("Смартфоны", "Категория для смартфонов")
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    category.add_product(product1)
    category.add_product(product2)
    assert len(category.products) == 2  # Проверяем, что в категории два продукта
    assert Category.product_count == 2  # Проверяем, что счетчик товаров увеличился
