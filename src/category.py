from src.product import Product


class Category:
    product_count = 0  # Класс-атрибут для подсчета продуктов

    def __init__(self, name):
        self.name = name
        self.__products = []  # Приватный атрибут для хранения списка продуктов

    def add_product(self, product):
        """Добавляет продукт в категорию, проверяя его тип."""
        if not isinstance(product, Product):
            raise TypeError(f"Можно добавлять только продукты или их наследники, а не {type(product).__name__}.")
        self.__products.append(product)  # Исправлено на self.__products

    @property
    def products(self):
        """Геттер для получения списка продуктов в виде строки."""
        return "\n".join(str(product) for product in self.__products)

    def __str__(self):
        """Строковое представление категории с количеством продуктов."""
        total_products = sum(product.rest for product in self.__products)  # Суммируем остатки всех продуктов
        return f"{self.name}, количество продуктов: {total_products} шт."

    def average_price(self):
        """Метод для подсчета среднего ценника всех товаров в категории."""
        try:
            total_price = sum(product.price * product.rest for product in self.__products)
            total_products = sum(product.rest for product in self.__products)
            average_price = total_price / total_products
        except ZeroDivisionError:
            return 0  # Если нет товаров, возвращаем 0
        return average_price
