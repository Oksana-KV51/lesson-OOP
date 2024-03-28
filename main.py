#Дополнительное задание:Ты разрабатываешь программное обеспечение для сети магазинов.
# Каждый магазин в этой сети имеет свои особенности, но также существуют общие
# характеристики, такие как адрес, название и ассортимент товаров. Ваша задача — создать
# класс Store, который можно будет использовать для создания различных магазинов.

class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.inventory = {}  # Словарь для хранения ассортимента товаров и их количества

    def add_item(self, item, quantity):
        """Добавляет товар в ассортимент магазина или обновляет его количество."""
        if item in self.inventory:
            self.inventory[item] += quantity
        else:
            self.inventory[item] = quantity

    def remove_item(self, item, quantity):
        """Удаляет определенное количество товара из ассортимента.
        Удаляет товар, если его количество становится равным нулю или меньше."""
        if item in self.inventory:
            self.inventory[item] -= quantity
            if self.inventory[item] <= 0:
                del self.inventory[item]

    def check_item(self, item):
        """Проверяет наличие товара в магазине и возвращает его количество."""
        return self.inventory.get(item, 0)

    def __str__(self):
        """Возвращает строковое представление магазина со всей необходимой информацией."""
        return f"Магазин '{self.name}' по адресу '{self.address}'. Ассортимент: {self.inventory}"

# Пример использования класса Store
store1 = Store("Продукты 24/7", "ул. Примерная, д. 10")
store1.add_item("Яблоки", 100)
store1.add_item("Бананы", 50)
store1.add_item("Молоко", 30)

print(store1)

store1.remove_item("Яблоки", 25)
print("После продажи яблок:", store1)

print("Количество молока в магазине:", store1.check_item("Молоко"))

store2 = Store("Книги Plus", "пр. Литературный, д. 15")
store2.add_item("Роман 'Война и мир'", 20)
store2.add_item("Справочник 'Python для начинающих'", 15)

print(store2)