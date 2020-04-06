"""
№1

У нас есть база данных зверей - AnimalDataBase.
Так же есть записи в реестре про зверей - records.

У каждого зверя есть набор стандартных атрибутов (см. класс Animal) и некоторые уникальные.
У млекопитающих (Mammal):
    - потомство (число).
У рептилий (Reptile):
    - является ли ядовитым? (число 1 - Да, 0 - Нет)
У птиц (Bird):
    - размах крыльев (число)
    - умеет ли издавать звуки? (число 1 - Да, 0 - Нет)
    - если умеет издавать звуки, то какие? (строка)

Нужно пройтись по всем записям в реестре (records) и сохранить всех зверей в базу данных AnimalDataBase.

Последовательность слов в каждой записии в реестре == последовательность параметров для каждого животного (сначала
базовые, потом уникальные).
Нужно определить какое это животное (по второму слову каждой записи в реестре) и правильно его сохранить со всеми
параметрами,
для этого нужно изменить метод `_create_animal` в AnimalDataBase

№2
Запросить ввод имени животного - `input()`
Напечатать строку с предложением ввести первую букву атрибута животного (показывать все возможные атрибуты (9 шт.).
Пример - `query_choice`
После ввода нужной буквы, вывести значение данного атрибута у животного с данным именем, либо напечатать что такого
атрибута у животного нету.
"""


class Animal:
    def __init__(self, name, animal_type, species, mass):
        self.name = name
        self.animal_type = animal_type
        self.species = species
        self.mass = mass


class Mammal(Animal):
    def __init__(self, name, animal_type, species, mass, children):
        super().__init__(name, animal_type, species, mass)
        self.children = children


class Reptile(Animal):
    def __init__(self, name, animal_type, species, mass, poison):
        super().__init__(name, animal_type, species, mass)
        self.poison = poison


class Bird(Animal):
    def __init__(self, name, animal_type, species, mass, wingspan, voice, list_voice=None):
        super().__init__(name, animal_type, species, mass)
        self.wingspan = wingspan
        self.voice = voice
        self.list_voice = list_voice


class AnimalDataBase:
    __animal_db = []

    def save_animal_to_db(self, animal):
        self.__animal_db.append(animal)

    def save_animals_from_records(self, records):
        for record in records:
            animal = self._create_animal(record)
            self.save_animal_to_db(animal)

    def _create_animal(self, record):
        animal_args = record.split(' ')
        if animal_args[1] == 'Mammal':
            return Mammal(animal_args[0], animal_args[1], animal_args[2], animal_args[3], animal_args[4])
        elif animal_args[1] == 'Reptile':
            return Reptile(animal_args[0], animal_args[1], animal_args[2], animal_args[3], animal_args[4])
        elif animal_args[1] == 'Bird':
            if len(animal_args) <= 6:
                return Bird(animal_args[0], animal_args[1], animal_args[2], animal_args[3], animal_args[4],
                            animal_args[5])
        return Bird(animal_args[0], animal_args[1], animal_args[2], animal_args[3], animal_args[4], animal_args[5],
                    animal_args[6:])

    def find_animal(self, name, first_char):
        is_animal_with_such_name = False
        for animal in self.__animal_db:
            if name == animal.name:
                animal_prop = char_dict[first_char]
                if hasattr(animal, animal_prop):
                    print(name, animal_prop, getattr(animal, animal_prop))
                else:
                    print('Animal - ', name, ' - hasn\'t such property')
                    is_animal_with_such_name = True
                    if not is_animal_with_such_name:
                        print('There is no animal with name - ', name)


records = [
    'Bob Mammal Bear 300 2',
    'Lucy Reptile Lizard 2 0',
    'Carl Reptile Cottonmouth 3 1',
    'Oliver Bird Ostrich 75 60 0',
    'Polly Bird Parrot 1 2 1 I want a cracker',
    'Doug Mammal Dog 20 4'
]

char_dict = {
    'a': 'animal_type',
    's': 'species',
    'm': 'mass',
    'c': 'children',
    'w': 'wingspan',
    'p': 'poison',
    'v': 'voice',
    'l': 'list_voice',
}

db = AnimalDataBase()
db.save_animals_from_records(records)
db.find_animal('Carl', 'm')




