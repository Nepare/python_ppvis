import json


class Warehouse:  # Склад, тут будем хранить кол-во всех растений
    namelist = ["яблони", "груши", "вишни", "сливы", "картофель", "морковь", "капуста", "перец"]
    house: dict

    def import_warehouse(self):
        with open("D:\\Projects\\2course\\ppvis\\sem2\\laba1\\lab1\\warehouse.json", 'r', encoding='utf-8') as f:
            self.house = json.loads(f.read())
            f.close()

    def nullify_warehouse(self):
        self.house = {
        'Яблоки': 0,
        'Груши': 0,
        'Вишни': 0,
        'Сливы': 0,
        'Картофель': 0,
        'Морковь': 0,
        'Капуста': 0,
        'Перец': 0
        }
        with open(r'D:\Projects\2course\ppvis\sem2\laba1\lab1\warehouse.json', 'w', encoding='utf-8') as f:
            json.dump(self.house, f, ensure_ascii=False, indent=2)
            f.close()

    def display_warehouse(self):
        if self.house.get("Яблоки") > 0:
            print("Яблоки: ", self.house.get("Яблоки"))
        if self.house.get("Груши") > 0:
            print("Груши: ", self.house.get("Груши"))
        if self.house.get("Вишни") > 0:
            print("Вишни: ", self.house.get("Вишни"))
        if self.house.get("Сливы") > 0:
            print("Сливы: ", self.house.get("Сливы"))
        if self.house.get("Картофель") > 0:
            print("Картофель: ", self.house.get("Картофель"))
        if self.house.get("Морковь") > 0:
            print("Морковь: ", self.house.get("Морковь"))
        if self.house.get("Капуста") > 0:
            print("Капуста: ", self.house.get("Капуста"))
        if self.house.get("Перец") > 0:
            print("Перец: ", self.house.get("Перец"))

    def export_warehouse(self):
        with open(r'D:\Projects\2course\ppvis\sem2\laba1\lab1\warehouse.json', 'w', encoding='utf-8') as f:
            json.dump(self.house, f, ensure_ascii=False, indent=2)
