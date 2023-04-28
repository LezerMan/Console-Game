class Game:

    def objects(self):
        global mw, sw, pw, army, wn, wn1, car
        army = ['Морпех', 'Солдат', 'Полицейский']
        wn = ['AK-47', 'M4A4']
        wn1 = ['Granade', 'Smoke']
        mw, sw, pw = ['Нету', 'Нету'], ['Нету', 'Нету'], ['Нету', 'Нету']
        car = ['Пустая']
        self.run()

    def run(self):
        for i in range(2):
            print()
        print(f'Морпех: Оружие - {mw[0]} | Доп.оружие - {mw[1]}',
              f'Солдат: Оружие - {sw[0]} | Доп.оружие - {sw[1]}',
              f'Полицейский: Оружие - {pw[0]} | Доп.оружие - {pw[1]}',
              f'Машина: {car[0]}',
              sep = '\n')
        self.choise()

    def choise(self):
        for i in range(2):
            print()
        print(f'1 - Выдать оружие\n2 - Выдать доп.оружие\n3 - Посадить в машину\n'
              f'Введите ответ: ', end ='')
        global choice
        choice = input()
        if choice in '12':
            self.choise_soldats()
        elif choice == '3':
            self.seat_car()
        else:
            self.choise()

    def choise_soldats(self):
        for i in range(2):
            print()
        global soldat
        if choice == '1':
            print(f'Какому солдату выдать оружие?\n1 - Морпеху\n2 - Солдату\n3 - Полицейскому\n'
                  f'Введите ответ: ', end ='')
            soldat = input()
            if soldat in '123':
                self.weapon()
            else:
                self.choise_soldats()
        elif choice == '2':
            print(f'Какому солдату выдать доп.оружие?\n1 - Морпеху\n2 - Солдату\n3 - Полицейскому\n'
                  f'Введите ответ: ', end='')
            soldat = input()
            if soldat in '123':
                self.add_weapon()
            else:
                self.choise_soldats()

    def weapon(self):
        for i in range(2):
            print()
        print(f'Какое выдать оружие?\n1 - AK-47\n2 - M4A4\n3 - Забрать оружие\n'
              f'Введите ответ: ', end='')
        elem = input()
        if elem in '12':
            if soldat == '1':
                mw[0] = wn[int(elem)-1]
            if soldat == '2':
                sw[0] = wn[int(elem)-1]
            else:
                pw[0] = wn[int(elem)-1]
            self.run()
        elif elem == '3':
            if soldat == '1':
                mw[0] = 'Нету'
            if soldat == '2':
                sw[0] = 'Нету'
            else:
                pw[0] = 'Нету'
            self.run()
        else:
            self.weapon()

    def add_weapon(self):
        for i in range(2):
            print()
        print(f'Какое выдать доп.оружие?\n1 - Гранату\n2 - Смоук\n3 - Забрать доп.оружие\n'
              f'Введите ответ: ', end='')
        elem = input()
        if elem in '12':
            if soldat == '1':
                mw[1] = wn1[int(elem)-1]
            if soldat == '2':
                sw[1] = wn1[int(elem)-1]
            else:
                pw[1] = wn1[int(elem)-1]
            self.run()
        elif elem == '3':
            if soldat == '1':
                mw[1] = 'Нету'
            if soldat == '2':
                sw[1] = 'Нету'
            else:
                pw[1] = 'Нету'
            self.run()
        else:
            self.add_weapon()

    def seat_car(self):
        for i in range(2):
            print()
        print(f'Кого посадить в машину?\n1 - Морпеха\n2 - Солдата\n3 - Полицейского\n4 - Освободить место\n'
              f'Введите ответ: ', end='')
        choise = input()
        if choise in '123':
            car[0] = army[int(choise)-1]
            self.run()
        elif choise == '4':
            car[0] = 'Нету'
            self.run()
        else:
            self.seat_car()


if __name__ == '__main__':
    game = Game()
    game.objects()