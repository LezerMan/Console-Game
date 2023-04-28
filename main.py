class Soldier:
    def __init__(self, name):
        self.name = name
        self.weapon = None
        self.add_weapon = None


class Car:
    def __init__(self):
        self.passengers = []

    def add_passenger(self, soldier):
        self.passengers.append(soldier)

    def remove_passenger(self):
        self.passengers.clear()


class Game:
    def __init__(self):
        self.army = [Soldier('Морпех'), Soldier('Солдат'), Soldier('Полицейский')]
        self.weapons = ['AK-47', 'M4A4']
        self.add_weapons = ['Granade', 'Smoke']
        self.car = Car()

    def run(self):
        for soldier in self.army:
            print(f'{soldier.name}: Оружие - {soldier.weapon} | Доп.оружие - {soldier.add_weapon}')
        print(f'Машина: {self.car.passengers[0].name if self.car.passengers else "Пустая"}')
        self.choose_action()

    def choose_action(self):
        print(f'1 - Выдать оружие\n2 - Выдать доп.оружие\n3 - Посадить в машину\n')
        choice = input('Введите ответ: ')
        if choice == '1':
            self.choose_soldier()
        elif choice == '2':
            self.choose_soldier_add()
        elif choice == '3':
            self.seat_soldier()
        else:
            self.choose_action()

    def choose_soldier(self):
        print(f'Какому солдату выдать оружие?\n1 - Морпеху\n2 - Солдату\n3 - Полицейскому\n')
        choice = input('Введите ответ: ')
        if choice in '123':
            soldier = self.army[int(choice) - 1]
            self.give_weapon(soldier)
        else:
            self.choose_soldier()

    def choose_soldier_add(self):
        print(f'Какому солдату выдать доп.оружие?\n1 - Морпеху\n2 - Солдату\n3 - Полицейскому\n')
        choice = input('Введите ответ: ')
        if choice in '123':
            soldier = self.army[int(choice) - 1]
            self.give_add_weapon(soldier)
        else:
            self.choose_soldier_add()

    def give_weapon(self, soldier):
        print(f'Какое выдать оружие?\n1 - AK-47\n2 - M4A4\n3 - Забрать оружие\n')
        choice = input('Введите ответ: ')
        if choice in '12':
            soldier.weapon = self.weapons[int(choice) - 1]
            self.run()
        elif choice == '3':
            soldier.weapon = None
            self.run()
        else:
            self.give_weapon(soldier)

    def give_add_weapon(self, soldier):
        print(f'Какое выдать доп.оружие?\n1 - Granade\n2 - Smoke\n3 - Забрать доп.оружие\n')
        choice = input('Введите ответ: ')
        if choice in '12':
            soldier.add_weapon = self.add_weapons[int(choice) - 1]
            self.run()
        elif choice == '3':
            soldier.add_weapon = None
            self.run()
        else:
            self.give_weapon(soldier)

    def seat_soldier(self):
        print(f'Кого посадить в машину?\n1-Морпеха\n2-Солдата\n3-Полицейского\n4-Освободить место\n')
        choice = input('Введите ответ: ')
        if choice in '123':
            self.car.add_passenger(self.army[int(choice)-1])
            self.run()
        else:
            self.car.remove_passenger()
            self.run()

if __name__ == '__main__':
    game = Game()
    game.run()

