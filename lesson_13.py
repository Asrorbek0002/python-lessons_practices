class CarIndustry:
    def __init__(self,cars,name):
        self.name=name
        self.cars=cars

    @classmethod
    def get_cars(cls,cars,name):
        print(cars,name)
        return cls(cars,name)

    def get_all_cars(self):
        return self.name,self.cars

    @staticmethod
    def calculate_engin_power(num1,num2):
        return num1+num2


s=CarIndustry.get_cars("test",12)
print(s.get_all_cars())
stm=s.calculate_engin_power(21,400)

print(isinstance(stm,CarIndustry))
print(isinstance(s,CarIndustry))


class Animal:
    vois='frefie ofb 3iiqib, Animal'
    @classmethod
    def get_vois(cls):
        return cls.vois

class Dog(Animal):
    vois='vow, vow'

class Cat(Animal):
    vois='miow'

a=Animal.get_vois()
d=Dog.get_vois()
m=Cat.get_vois()

print(a)
print(d)
print(m)



# #ToDo
# from datetime import datetime
#
# class ToDoList:
#     def __init__(self):
#         self.tasks = []
#     def show_menu(self):
#         print("\nTo-Do List:")
#         print("1. Vazifa qo'shish")
#         print("2. Vazifalarni ko'rish")
#         print("3. Vazifani o'chirish")
#         print("4. Chiqish")
#
#     def add_task(self):
#         task = input("Vazifa kiriting: ")
#         current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         self.tasks.append({"task": task, "date": current_date})
#         print(f"'{task}' vazifasi qo'shildi ({current_date}).")
#
#     def view_tasks(self):
#         if not self.tasks:
#             print("Hozircha vazifalar yo'q.")
#         else:
#             print("\nVazifalar:")
#             for i, task_info in enumerate(self.tasks, 1):
#                 print(f"{i}. {task_info['task']} (Qo'shilgan sana: {task_info['date']})")
#
#     def remove_task(self):
#         self.view_tasks()
#         if self.tasks:
#             try:
#                 task_num = int(input("O'chirmoqchi bo'lgan vazifaning raqamini kiriting: "))
#                 removed_task = self.tasks.pop(task_num - 1)
#                 print(f"'{removed_task['task']}' vazifasi o'chirildi!")
#             except (ValueError, IndexError):
#                 print("Noto'g'ri raqam kiritildi.")
#
#     def run(self):
#         while True:
#             self.show_menu()
#             choice = input("Tanlovingiz: ")
#             if choice == "1":
#                 self.add_task()
#             elif choice == "2":
#                 self.view_tasks()
#             elif choice == "3":
#                 self.remove_task()
#             elif choice == "4":
#                 print("Dastur tugatildi. Hayr!")
#                 break
#             else:
#                 print("Noto'g'ri tanlov! Qayta urinib ko'ring.")
#
#
# if __name__ == "__main__":
#     todo_app = ToDoList()
#     todo_app.run()
#
















