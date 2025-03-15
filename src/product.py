from src.base_product import BaseProduct


class CreationInfoMixin:
    def __init__(self, *args, **kwargs):
        class_name = self.__class__.__name__
        params = ", ".join([repr(arg) for arg in args])
        params += ", " + ", ".join([f"{a}={b}" for a, b in kwargs.items()])
        print(f"Реализован объект '{class_name}' с параметрами: {params}")


class Product(BaseProduct, CreationInfoMixin):
    def __init__(self, name, price, rest):
        super().__init__(name, price, rest)
        self.name = name  # Название продукта
        self.price = float(price)  # Цена продукта
        self.rest = int(rest)  # Остаток продукта на складе
        self.__price = self.price  # Скрытый атрибут для цены

    def __repr__(self):
        return f"Product(name={self.name}, price={self.price}, rest={self.rest})"

    def __str__(self):
        """Строковое представление продукта."""
        return f"{self.name}, {self.price:.2f} руб. Остаток: {self.rest} шт."

    def __add__(self, other):
        """Сложение двух продуктов для вычисления их полной стоимости."""
        if type(self) is not type(other):
            raise TypeError(
                f"Нельзя складывать продукты разных классов: {type(self).__name__} и {type(other).__name__}."
            )
        return (self.price * self.rest) + (other.price * other.rest)

    @property
    def price(self):
        """Геттер для получения цены."""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Сеттер для установки новой цены с проверкой."""
        if new_price > 0:
            self.__price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")

    @classmethod
    def new_product(cls, product_info):
        """Класс-метод для создания нового продукта из словаря."""
        name = product_info.get("name")
        price = product_info.get("price")
        rest = product_info.get("rest")
        return cls(name, price, rest)

    def get_total_value(self):
        """Метод для получения общей стоимости остатка продукта."""
        return self.price * self.rest
