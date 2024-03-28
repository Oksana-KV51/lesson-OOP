#Задача: Создай класс Task, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус
# (выполнено/не выполнено). Реализуй функцию для добавления задач, отметки
# выполненных задач и вывода списка текущих (не выполненных) задач.

class Task:
    # Конструктор класса с атрибутами: описание задачи(description),
    # срок выполнения (deadline) и статус выполнения - status
    # (по умолчанию не выполнено - False)
    def __init__(self, description, deadline, status=False):
        self.description = description
        self.deadline = deadline
        self.status = status

    # Метод для отображения информации о задаче
    def __str__(self):
        return f"{self.description}, Deadline: {self.deadline}, Status: {'Completed' if self.status else 'Not Completed'}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    # Метод для добавления новой задачи
    def add_task(self, description, deadline):
        self.tasks.append(Task(description, deadline))

    # Метод для отметки задачи как выполненной
    def complete_task(self, description):
        for task in self.tasks:
            if task.description == description:
                task.status = True
                print(f"Task '{description}' marked as completed.")
                return
        print(f"Task '{description}' not found.")

    # Метод для вывода списка невыполненных задач
    def show_current_tasks(self):
        print("Current Tasks:")
        for task in self.tasks:
            if not task.status:
                print(task)

# Пример использования
task_manager = TaskManager()
task_manager.add_task("Сделать уборку", "2023-04-30")
task_manager.add_task("Купить продукты", "2023-04-25")
task_manager.add_task("Позвонить другу", "2023-04-24")

task_manager.complete_task("Купить продукты")

task_manager.show_current_tasks()
