# разбор ДЗ дополнительной задачи

class Store():
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_items(self, item_name, price):
        self.items[item_name] = price
        print(f'товар {item_name} был добавлен в {self.name}')

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f'товар {item_name} удален из {self.name}')

    def get_price(self, item_name):
        return self.items.get(item_name)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f'цена на товар {item_name} обновлена в {self.name}')
        else:
            print(f'товар {item_name} ненайден')


stor1 = Store(name = 'пяторочка', address = 'Фрунзе 1')
stor2 = Store(name = 'магнит', address = 'Ленина 20')
stor3 = Store(name = 'перекрестока', address = 'Лесная 1')

stor1.add_items(item_name = 'хлеб', price = 67)
stor1.add_items(item_name = 'молоко', price = 120)
stor1.add_items(item_name = 'конфеты', price = 300)

stor1.remove_item('хлеб')
print(stor1.get_price('молоко'))
stor1.update_price(item_name = 'конфеты', new_price = 280)