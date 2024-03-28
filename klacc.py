# Определите класс Accoun, имитирующий банковский счет.
# Клаа должен включать отрибуты для хранения  ИД владельца,
# баланс счета и методы для депозита (пополнения) и снятия средств, если
#на счету достаточно средств


class Account():
    def __init__(self, id, balance=0):
        self.id = id
        self.balance = balance

    def depos(self, money):
        if money > 0:
            self.balance += money
            print(f'вы пополнили. Сумма на счету - {self.balance}')

    def withdraw(self, money):
        if money > self.balance:
            print('недостаточно средств')
        elif money <= self.balance:
            self.balance -= money
            print(f'вы успешно сняли {money}. Остаток на счете - {self.balance}')

    def all_balance(self):
        print(f'Текущий баланс - {self.balance}')

man = Account(id= '12323132', balance= 600)
man.all_balance()
man.withdraw(450)
man.withdraw(800)
man.depos(23000)