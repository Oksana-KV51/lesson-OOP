# разбор ДЗ

class Task():
    def __init__(self):
        self.tasks = []

    def add_task(self, deadline, description):
        self.tasks.append({'deadline': deadline,
                          'description': description, 'status': 'не выполнено'})

    def complete_task(self, description):
            for task in self.tasks:
                task['description'] == description
                print(f'задача {description} выполнена')
            else:
                print(f'задача {description} не найдена')

    def show_tasks(self):
        print('текущие задачи')
        for task in self.tasks:
            if task['status'] == 'не выполнено':
                print(f"{task['description']} - {task['deadline']}")

t = Task()
t.add_task(deadline = "01.06.2024", description = "написать письмо")
t.add_task(deadline = "01.07.2024", description = "сдать нормы ГТО")
t.add_task(deadline = "01.08.2024", description = "сходить к врачу")
t.show_tasks()
t.complete_task("сдать нормы ГТО")