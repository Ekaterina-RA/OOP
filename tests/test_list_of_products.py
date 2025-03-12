from src.list_of_products import LawnGrass, Smartphone
from src.product import Product


def test_product_creation():
    product = Product("Товар", 100.0, 10)
    assert product.name == "Товар"
    assert product.price == 100.0
    assert product.rest == 10


def test_smartphone_creation():
    smartphone = Smartphone("iPhone 13", 99999.99, 5, 95, "iPhone 13", 128, "Black")
    assert smartphone.name == "iPhone 13"
    assert smartphone.price == 99999.99
    assert smartphone.rest == 5
    assert smartphone.efficiency == 95
    assert smartphone.model == "iPhone 13"
    assert smartphone.memory == 128
    assert smartphone.color == "Black"


def test_lawn_grass_creation():
    grass = LawnGrass("Газонная Трава", 1500.0, 20, "Россия", 14, "Зеленый")
    assert grass.name == "Газонная Трава"
    assert grass.price == 1500.0
    assert grass.rest == 20
    assert grass.country == "Россия"
    assert grass.germination_period == 14
    assert grass.color == "Зеленый"


def test_product_addition():
    product1 = Product("Товар 1", 100.0, 5)
    product2 = Product("Товар 2", 200.0, 10)
    total_value = product1 + product2
    assert total_value == (100.0 * 5 + 200.0 * 10)


def test_smartphone_addition():
    smartphone1 = Smartphone("Samsung Galaxy S21", 70000.0, 7, 90, "S21", 128, "White")
    smartphone2 = Smartphone("Xiaomi Mi 11", 30000.0, 10, 85, "Mi 11", 256, "Blue")
    total_value = smartphone1 + smartphone2
    assert total_value == (70000.0 * 7 + 30000.0 * 10)
