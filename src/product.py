class Product:
    def __init__(self, name, description, price, quantity):
        """Класс продукты"""
        name: str
        description: str
        price: float
        quantity: int

        self.name = name  # Название товара
        self.description = description  # Описание товара
        self.price = price  # Цена товара
        self.quantity = quantity  # Количество в наличии

    def products(self):
        return (
            f"Product(name={self.name}, description={self.description}, price={self.price}, quantity={self.quantity})"
        )
