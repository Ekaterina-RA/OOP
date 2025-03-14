from abc import ABC, abstractmethod


class BaseProduct(ABC):
    @abstractmethod
    def __init__(self, name, price, rest):
        self.name = name  # Название продукта
        self.price = float(price)  # Цена продукта
        self.rest = int(rest)  # Остаток продукта на складе

    @abstractmethod
    def __str__(self):
        """Строковое представление продукта."""
        pass

    @abstractmethod
    def get_total_value(self):
        """Метод для получения общей стоимости остатка продукта."""
        pass
