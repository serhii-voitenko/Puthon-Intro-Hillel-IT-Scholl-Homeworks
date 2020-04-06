import re
import json


class Item:
    """ класс создаёт заметку и при вызове метода, показывает её """
    def __init__(self, name, done):
        self.name = name
        self.done = done

    def get_display(self):
        return f'{self.name}: {self.done}'


class TodoList:
    """ класс самого списка """
    """ выбор языка вначале """
    eng_regexp = r'^[A-Za-z]'
    ru_regexp = r'^[А-Яа-я]'
    lang_map = {
        'ENG': eng_regexp,
        'RU': ru_regexp
    }

    def __init__(self, owner_full_name, file_path, lang='ENG'):
        """ указывается юзер, название будущего файла, и путь его сохранения. при его отстутствии он создаётся """
        self.owner_full_name = owner_full_name
        self.file_path = file_path
        self.act_regex = self.lang_map[lang]
        try:
            self.tasks = self.get_existing_tasks()
        except (FileExistsError, FileNotFoundError):
            self.tasks = {}

    def get_existing_tasks(self):
        """ метод открытия файла """
        with open(self.file_path, 'r') as file:
            return json.load(file)

    def write_to_file(self):
        """ метод записи в файл """
        with open(self.file_path, 'a+') as file:
            json.dump(self.tasks, file)
            json.dump(self.owner_full_name, file)

    def add_task(self, task_name, done):
        """ метод добавления заметки в список, проверка на соответствие введённой заметки языку """
        if re.match(self.act_regex, task_name):
            task = Item(task_name, done)
            self.tasks.update({task.name: task.done})
        else:
            raise BaseException('Not match reg exp(((')

    def show_tasks(self):
        """ показывает заметки """
        tasks = []
        for k, v in self.tasks.items():
            tasks.append(Item(k, v).get_display())
        print(' | '.join(tasks))

    def make_task_done(self, task_name):
        """ отмечает выполненную заметку как выполненную """
        self.tasks[task_name] = True

    def show_undone_tasks(self):
        """ показывает, что ещё не выполнено """
        undone_tasks = []
        for k, v in self.tasks.items():
            if not v:
                undone_tasks.append(Item(k, v).get_display())
        print(' | '.join(undone_tasks))

    def start_list(self):
        """ консольный интерфейс взаимодействия с юзером """
        while True:
            opt = input('Input option add/show_all/show_undone/make_done/exit ')
            if opt == 'exit':
                self.write_to_file()
                break
            elif opt == 'add':
                self.add_task(input('Task_name '), bool())
            elif opt == 'show_all':
                self.show_tasks()
            elif opt == 'show_undone':
                self.show_undone_tasks()
            elif opt == 'make_done':
                self.make_task_done(input('Task_name '))


my_task_list = TodoList('Serhii Voitenko', 'tasks.json')
my_task_list.start_list()
