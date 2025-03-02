from src.product import Product


class Category:
    category_count = 0  # Статический атрибут для подсчета категорий
    product_count = 0  # Статический атрибут для подсчета товаров

    def __init__(self, name: str, description: str, products=None):
        """Класс для категории товаров"""

        self.name = name
        self.description = description
        self.products = products if products is not None else []  # Список товаров категории
        Category.category_count += 1  # Увеличиваем счетчик категорий
        Category.product_count += len(self.products)

    def add_product(self, product: Product):
        self.products.append(product)  # Добавление товара в категорию
        Category.product_count += 1  # Увеличиваем счетчик товаров

    def category(self):
        return f"Category(name={self.name}, description={self.description}, products={self.products})"
