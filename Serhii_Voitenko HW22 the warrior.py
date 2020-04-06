"""
Воин
Создать класс воина, создать 2 или больше объектов воина с соответствующими воину атрибутами. Реализовать методы,
которые позволять добавить силы воину, улучшить оружие. Реализовать возможность драки 2х воинов с потерей здоровья,
приобретения опыта (можно магические методы, можно кастомные).
"""


class Warrior:
    """ Класс игрового персонажа """
    def __init__(self, name, power):
        self.name = name
        self.hp = 100
        self.exp = 0
        self.power = power

    def attack(self, another_warrior):
        another_warrior.hp = another_warrior.hp - self.power
        self.exp += 40
        return another_warrior.hp, self.exp

    def heal(self):
        self.hp += 15
        return self.hp

    def buff(self):
        self.power += 5
        return self.power


class Battle:
    """ Битва """
    def __init__(self, *args):
        self.war1 = args[0]
        self.war2 = args[1]

    def start(self):
        self.war1.attack(war2)
        self.war2.heal()
        self.war2.attack(war1)
        self.war1.buff()
        self.war1.attack(war2)
        return print(f'Характеристики воина {war1.name}: \tЗдоровье: {war1.hp}, \tОпыт: {war1.exp}, \tСила: {war1.power},'
                     f'\nХарактеристики воина {war2.name}: \tЗдоровье: {war2.hp}, \tОпыт:{war2.exp}, \tСила: {war2.power}')


war1 = Warrior('Orc', 15)
war2 = Warrior('Elf', 12)


Battle(war1, war2).start()




