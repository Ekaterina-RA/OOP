from src.category import Category
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
