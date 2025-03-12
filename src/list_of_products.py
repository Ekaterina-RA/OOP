from src.product import Product


class Smartphone(Product):
    def __init__(self, name, price, rest, efficiency, model, memory, color):
        super().__init__(name, price, rest)  # Инициализируем родительские атрибуты
        self.efficiency = efficiency  # Производительность
        self.model = model  # Модель
        self.memory = memory  # Объем встроенной памяти
        self.color = color  # Цвет

    def __str__(self):
        """Строковое представление смартфона."""
        return (
            f"{super().__str__()}, Эффективность {self.efficiency}, Модель: {self.model}, "
            f"Память: {self.memory} ГБ, Цвет: {self.color}"
        )


class LawnGrass(Product):
    def __init__(self, name, price, rest, country, germination_period, color):
        super().__init__(name, price, rest)  # Инициализируем родительские атрибуты
        self.country = country  # Страна-производитель
        self.germination_period = germination_period  # Срок прорастания
        self.color = color  # Цвет

    def __str__(self):
        """Строковое представление газонной травы."""
        return (
            f"{super().__str__()}, Страна: {self.country}, Время прорастания: "
            f"{self.germination_period} дней, Цвет: {self.color}"
        )
