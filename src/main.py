from src.category import Category
from src.product import Product

if __name__ == "__main__":
    category = Category("Смартфоны")

    product1 = Product("Samsung Galaxy S23 Ultra", 180000.0, "256GB, Серый цвет, 200MP камера", 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)

    print(category.products)
    product4 = Product("Телевизор 55 QLED 4K", 123000.0, "Фоновая подсветка", 7)
    category.add_product(product4)
    print(category.products)
    print(category.product_count)


# Пример использования
if __name__ == "__main__":
    # Создаем продукт с помощью класс-метода
    product_info = {"name": "Смартфон", "price": 8000, "description": "Современный смартфон с 64ГБ памяти", "rest": 20}

    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "rest": 5,
        }
    )
    print(new_product.name)
    print(new_product.description)
    print(new_product.price)
    print(new_product.rest)

    new_product.price = 800
    print(new_product.price)
    # Проверка сеттера с отрицательной ценой
    new_product.price = -100
    print(new_product.price)
