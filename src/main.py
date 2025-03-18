from src.category import Category
from src.list_of_products import LawnGrass, Smartphone
from src.product import Product

if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", 180000.0, 5)
    product2 = Product("Iphone 15", 200000.0, 7)
    product3 = Product("Xiaomi Redmi Note 11", 175000.3, 3)

    print(str(product1))
    print(str(product2))
    print(str(product3))

    category_1 = Category("Смартфоны")

    print(str(category_1))

    print(category_1.products)

    print(product1 + product2)
    print(product1 + product3)
    print(product2 + product3)

# Пример создания объектов
if __name__ == "__main__":
    smartphone = Smartphone("Samsung Galaxy S23 Ultra", 180000.0, 5, 95.5, "S23 Ultra", 256, "Grey")
    print(smartphone.name)
    print(smartphone.price)
    print(smartphone.rest)
    print(smartphone.efficiency)
    print(smartphone.model)
    print(smartphone.memory)
    print(smartphone.color)

    grass = LawnGrass("Газонная трава", 500.0, 20, "Russia", "7 дней", "Green")

    print(grass.name)
    print(grass.price)
    print(grass.rest)
    print(grass.country)
    print(grass.germination_period)
    print(grass.color)
try:
    smartphone_1 = Smartphone("Iphone 15", 210000.0, 8, 98.2, "15", 512, "Gray space")
    smartphone_2 = Smartphone("Xiaomi Redmi Note 11", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")
    grass_1 = LawnGrass("Газонная трава 1", 1500, 100, "Россия", 14, "Зеленый")
    grass_2 = LawnGrass("Газонная трава 2", 450.0, 15, "США", "5 дней", "Темно-зеленый")

    smartphone_sum = smartphone_1 + smartphone_2
    print(smartphone_sum)

    grass_sum = grass_1 + grass_2
    print(grass_sum)
    # Попытка сложить разные классы
    total_cost_invalid = smartphone_1 + grass_1  # Это вызовет ошибку
except TypeError:
    print("Возникла ошибка TypeError при попытке сложения")
else:
    print("Не возникла ошибка TypeError при попытке сложения")
    category_smartphones = Category("Смартфоны", "Высокотехнологичные смартфоны", [smartphone_1, smartphone_2])
    category_grass = Category("Газонная трава", "Различные виды газонной травы", [grass_1, grass_2])

    category_smartphones.add_product(smartphone_2)
    print(category_smartphones.products)
    print(Category.product_count)
