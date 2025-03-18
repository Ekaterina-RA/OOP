from abc import ABC, abstractmethod


class BaseProduct(ABC):
    @abstractmethod
    def get_total_value(self):
        """Метод для получения общей стоимости остатка продукта."""
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, product_info):
        """Класс-метод для создания нового продукта из словаря."""
        pass
