class Product:
    def __init__(self, name, price, description, rest):
        name: str
        price: float
        description: str
        rest: int
        self.name = name
        self.__price = price
        self.description = description
        self.rest = rest

    def __list_of_products__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.rest} шт."

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
        description = product_info.get("description")
        rest = product_info.get("rest")

        return cls(name, price, description, rest)

    def __product_info__(self):
        """Метод для отображения информации о продукте."""
        return f"{self.name}, {self.price} руб. Остаток: {self.rest} шт."
