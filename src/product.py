class Product:
    def __init__(self, name, price, rest):
        name: str
        price: float
        rest: int
        self.name = name  # Название продукта
        self.price = float(price)  # Цена продукта
        self.rest = int(rest)  # Остаток продукта на складе

    def __str__(self):
        """Строковое представление продукта."""
        return f"{self.name}, {self.price} руб. Остаток: {self.rest} шт."

    def __add__(self, other):
        """Сложение двух продуктов для вычисления их полной стоимости."""
        if isinstance(other, Product):
            return (self.price * self.rest) + (other.price * other.rest)
        return NotImplemented

    @property
    def price(self):
        """Геттер для получения цены."""
        return self.__price

    @price.setter
    def price(self, new_price):
        new_price: float

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

    def __product_info__(self):
        """Метод для отображения информации о продукте."""
        return f"{self.name}, {self.price} руб. Остаток: {self.rest} шт."
