# ________________Сказка про Колобка_______________________


class Hero:
    """ Присваивает имя герою """
    def __init__(self, name):
        self.name = name


class Colobok(Hero):
    """ Убегает от всех и поёт песню """

    def runaway(self, *args):
        print(self.name + ' run away from ' + ','.join(args))

    def meeting(self, *args):
        print(self.name + ' meets ' + ','.join(args))

    def sing(self):
        print(f'{self.name} sing his song.')


class Babka(Hero):
    """ Собирает ингридиенты и печёт Колобок """
    def bake_colobok(self):
        print(f'{self.name} bakes Kolobok.')
        return Colobok('Kolobok')

    def gathering(self):
        print(f'{self.name} searching and finding ingridients.')


class Ded(Hero):
    """ Просит бабку испечь колобок """
    def tel_babka_about_colobok(self):
        print(f'{self.name} ask Babka to bake the Kolobok.')


class Enemy(Hero):
    """ Животина, которая хочет сожрать Колобок """
    def eat(self):
        print(f'{self.name} wants to eat the Kolobok')

    def swallowing(self):
        print(f'{self.name} said: It was a good song, Kolobok! Seat please on my tongue and repeat it!\n'
              f'And swallowed Kolobok!')


class Tale:
    """ Действия сказки """
    def __init__(self, *args):
        self.babka = babka
        self.ded = ded
        self.colobok = None
        self.hare = hare
        self.wolf = wolf
        self.bear = bear
        self.fox = fox

    def babkin_dom(self):
        self.ded.tel_babka_about_colobok()
        self.babka.gathering()
        self.colobok = self.babka.bake_colobok()

    def start(self):
        self.babkin_dom()
        self.colobok.runaway(babka.name)

        self.colobok.meeting(hare.name)
        self.hare.eat()
        self.colobok.sing()
        self.colobok.runaway(hare.name)

        self.colobok.meeting(wolf.name)
        self.wolf.eat()
        self.colobok.sing()
        self.colobok.runaway(wolf.name)

        self.colobok.meeting(bear.name)
        self.bear.eat()
        self.colobok.sing()
        self.colobok.runaway(bear.name)

        self.colobok.meeting(fox.name)
        self.fox.eat()
        self.colobok.sing()
        self.fox.swallowing()


ded = Ded('Ded')
babka = Babka('Babka')
colobok = Colobok
hare = Enemy('Hare')
wolf = Enemy('Wolf')
bear = Enemy('Bear')
fox = Enemy('Fox')


Tale().start()
