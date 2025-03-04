from src.product import Product


class Category:
    product_count = 0  # Класс-атрибут для подсчета продуктов

    def __init__(self, name):
        self.name = name
        self.__products = []  # Приватный атрибут для хранения списка продуктов

    def add_product(self, product):
        """Добавляет продукт в категорию и увеличивает счетчик продуктов."""
        if isinstance(product, Product):
            self.__products.append(product)  # Добавляем продукт в список
            Category.product_count += 1  # Увеличиваем счетчик продуктов
        else:
            raise ValueError("Только объекты класса Product добавляются.")

    @property
    def products(self):
        """Геттер для получения списка продуктов в виде строки."""
        return "\n".join(
            f"{product.name}, {product.price} руб. Остаток: {product.rest} шт." for product in self.__products
        )
