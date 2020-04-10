# _____BANKOMAT/ACC______
"""
ЧТО СДЕЛАНО
Реализован класс банкомата (вероятно, нужно будет добавить методов или атрибутов)
Реализован класс аккаунта (вероятно, нужно будет добавить методов или атрибутов)
Реализован (не полностью) класс банка
ЧТО НУЖНО СДЕЛАТЬ
Дописать класс банка:
у банка должны быть сервисные методы
 удаления банкомата из списка (вероятно, прийдется переделать его на словарь для простоты) банка
 Аварийное сохранение данных о банкоматах и аккаунтах (в разные файлы)
 Удаление аккаунтов из списка аккаунтов

  А так же менюшка - перевод стредств между аккаунтами и создание аккаунта (если будет муза - можно добавить что-то свое)
2 Написать функцию или класс, где создастся объект банка и банкомата этого банка, так же будет меню с выбором куда юзер
 хочет пойти.
    Если у него нет (обработка ошибок) аккауунта - соббщение о том, что нужно пойти сначала в банк и создать аккаунт.
    Если аккаунт есть -  у юзера есть выбор куда пойти банк или банкомат. При выборе банка - будет меню банка,
    если банкома - банкомата

Менять текущие методы можно по потребности
"""
import json


class PersonACC:
    """
    Потом будет создаваться в классе БАНК
    А так это аккаунт человека в банке
    """

    def __init__(self, inn, limit, passport_data=None):
        self.inn = inn
        self.set_limit = limit
        self.passport_data = passport_data
        self.__person_id = self.__generate_id()
        self.__login = f'{self.passport_data["full_name"]}'
        self.__pwd = f'{self.__person_id}'
        self.__curr_money = 0

    def __generate_id(self):
        """ генератор пароля пользователя """
        return f'{self.inn + self.passport_data["number"]}'

    @property
    def login(self):
        return self.__login

    @property
    def password(self):
        return self.__pwd

    @property
    def cur_money(self):
        """ текущий счёт - в банкомате"""
        return self.__curr_money

    def get_money(self, val):
        """ метод для снятия денег - в банкомате"""
        self.__curr_money -= val
        return self.__curr_money

    def add_money(self, val):
        """ метод для пополнения средств - в банке"""
        if val <= self.set_limit:
            self.__curr_money += val
            return self.__curr_money
        print('Set limit is low')

    def check_money_limit(self):
        """ проверка текущего лимита в банкомате """
        return f'Current limit: {self.set_limit}, current money: {self.__curr_money}'

    def to_dict(self):
        """ запись данных аккаунта в файл - в случае аварии """
        return {
            'inn': self.inn,
            'limit': self.set_limit,
            'passport_data': self.passport_data
        }


class ATM:
    """
    класс Банкомата
    """

    def __init__(self, bank_name, name):
        self.bank = bank_name
        self.name = name
        self.bank.add_atm(self)

    def __check_bank(self):
        """
        Проверка рабочий ли банкомат
        :return: bool
        """
        return self in self.bank.atm_list

    def __connect_to_bank(self, person_acc):
        """
        Метод проверяет рабочий ли банкомат и визывает логин аккаунта в банке, иначе возвращает фолс
        :param person_acc: аккаунт человека
        :return: буль
        """
        if self.__check_bank():
            return self.bank.login(person_acc)
        return False

    def main(self, person_acc):
        """
        Метод проверяет коннект к банку,если все гуд - заходит в меню банкомата
        :param person_acc: аккаунт человека
        :return: None
        """
        if self.__connect_to_bank(person_acc):
            while True:
                operation = input('Input operation: '
                                  '[get] - to get money, '
                                  '[add] - to add money, '
                                  '[balance] - to check the balance, '
                                  '[exit] - to finish the operation, ')
                if operation == 'get':
                    money = input('Input value to get: ')
                    self.bank.get_money(person_acc, money)
                elif operation == 'balance':
                    self.bank.get_acc_balance(person_acc)
                elif operation == 'exit':
                    print(f'By-by {person_acc.login}')
                    break
            bank.accounts.update({str(person_acc.login): person_acc})
            return person_acc
        print('Login failed.')


class Bank:
    """
    класс Банка
    создаётся список банкоматов и аккаунтов
    """

    def __init__(self, name):
        self.name = name
        self.__atm_list = []
        self.__accounts = {}

    @property
    def atm_list(self):
        """ список банкоматов """
        return self.__atm_list

    @property
    def accounts(self):
        """ список аккаунтов """
        return self.__accounts

    def add_atm(self, new_atm):
        """
        Метод для добавления нового банкомата в список банкоматов банка
        :return:
        """
        self.__atm_list.append(new_atm)
        return self.__atm_list

    def atm_to_delete(self, old_atm):
        """ удаление банкомата """
        self.__atm_list.remove(old_atm)

    def create_person_acc(self, person_acc):
        """
        Метод создает аккаунт в банке,добавляя его в хранилище аккаунтов банка
        :param args:
        :param kwargs:
        :return:
        """
        create_inn = str(input('Enter your INN: '))
        create_money_limit = int(input('Enter the money limit: '))
        create_passport_data = {"full_name": str(input('Enter your full name: ')),
                                "number": str(input('Enter your passport number: '))}
        person_acc = PersonACC(create_inn, create_money_limit, create_passport_data)
        self.__accounts.update({str(person_acc.login): person_acc})
        print(f'Your login: {person_acc.login}, your password: {person_acc.password}')
        return person_acc

    def login(self, person_acc):
        """
        Метод для логина, сравнивает пароли аккаунта и банка, если гуд - вернет тру
        :return: буль
        """
        bank_side_acc = input('Input your login: ')
        if bank_side_acc == person_acc.login:
            bank_side_acc_password = input('Input your password: ')
            if bank_side_acc_password == person_acc.password:
                return True
        return False

    def get_money(self, person_acc, money):
        """
        Метод для снятия денег с аккаунта
        :return:
        """
        if person_acc.cur_money > int(money):
            person_acc.get_money(int(money))
            print(f'Now account balance is: {person_acc.cur_money}')
        else:
            print('Your account balance is low. Please add money before continue the operation.')

    def add_money(self, person_acc, money):
        """
        Метод для добавления денег
        :return:
        """
        person_acc.add_money(int(money))
        print(f'Now account balance is: {person_acc.cur_money}')

    def get_acc_balance(self, person_acc):
        """
        Метод для показывания текущего баланса
        :return:
        """
        print(person_acc.check_money_limit())

    def send_money(self, person_acc, another_person_acc, money):
        """ метод отправки денег другому аккаунту """
        if another_person_acc in self.__accounts:
            self.get_money(person_acc, money)
            self.add_money(self.__accounts[another_person_acc], money)
            self.__accounts.update({str(person_acc.login): person_acc})
            self.__accounts.update({str(another_person_acc): self.__accounts[another_person_acc]})
            print(f'Now {another_person_acc} has {self.accounts[another_person_acc].cur_money}')
        else:
            print('Not valid account to send')

    def delete_atm(self, atm_to_delete):
        """ удаление банкомата из списка """
        if atm_to_delete in self.__atm_list:
            self.__atm_list.remove(atm_to_delete)
            return

    def delete_acc(self, person_acc):
        """ метод удаления аккаунта """
        if person_acc.login in self.__accounts:
            print(f'Account {person_acc.login} was deleted')
            del self.__accounts[person_acc.login]
            return

    def backup(self):
        """ аварийное сохранение данных """
        with open('ATM_backup.txt', 'w') as file:
            file.write(str(len(self.__atm_list)))
        with open('Accounts_backup.txt', 'w') as file:
            data = [person_acc.to_dict()]
            json.dump(data, file)

    def main(self, person_acc):
        """
        :param person_acc: аккаунт человека
        :return: None
        """
        while True:
            operation = input('Input operation:'
                              '[get] - to get money, '
                              '[add] - to add money, '
                              '[send] - to send money another person, '
                              '[balance] - to check the balance, '
                              '[delete] - to delete your account, '
                              '[exit] - to finish the operation, ')
            if operation == 'get':
                money = input('Input value to get ')
                self.get_money(person_acc, money)
            elif operation == 'add':
                money = input('Input value to add ')
                self.add_money(person_acc, money)
            elif operation == 'send':
                money = input('Input value to send another person ')
                another_person_acc = str(input('Input account to send a value '))
                self.send_money(person_acc, another_person_acc, money)
            elif operation == 'balance':
                self.get_acc_balance(person_acc)
            elif operation == 'delete':
                self.delete_acc(person_acc)
            elif operation == 'exit':
                print(f'By-by {person_acc.login}')
                break
        self.__accounts.update({str(person_acc.login): person_acc})
        return person_acc


class UserVisit:
    """ класс обращения пользователя """

    def __init__(self, bank_name, atm_name):
        self.bank_name = bank_name
        self.atm_name = atm_name

    def start(self, person_acc=None):
        """ вход в систему юзера """
        self.bank_name = Bank(self.bank_name)
        self.atm_name = ATM(self.bank_name, self.atm_name)
        try:
            self.bank_name.login(person_acc) is True
        except AttributeError:
            print(f'You should create an account before start.')
            created_acc = self.bank_name.create_person_acc(person_acc)
            self.bank_or_atm(created_acc)

    def continue_work(self, person_acc):
        """ повторный вход в систему, при вводе неверных данных происходит бэкап данных """
        if self.bank_name.login(person_acc) is True:
            while True:
                order = input('Would you like to visit [bank] or [atm]? Input [exit] to exit ')
                if order == 'bank':
                    self.bank_name.main(person_acc)
                elif order == 'atm':
                    self.atm_name.main(person_acc)
                elif order == 'exit':
                    return self.continue_work(person_acc)
        self.bank_name.backup()
        print(f'You should create an account before start.')
        created_acc = self.bank_name.create_person_acc(person_acc)
        self.bank_or_atm(created_acc)

    def bank_or_atm(self, created_acc):
        """ выбор куда идти, если банкомата нет в списке - бэкап данных """
        global person_acc
        try:
            self.atm_name in self.bank_name.atm_list
        except Exception:
            self.bank_name.backup()
            raise BaseException('Something went wrong.. ')
        order = input('Would you like to visit [bank] or [atm]? ')
        if order == 'bank':
            person_acc = self.bank_name.main(created_acc)
        elif order == 'atm':
            person_acc = self.atm_name.main(created_acc)
        self.continue_work(person_acc)


bank = Bank('Privat')
bank.add_atm('1')
user = UserVisit(bank, '1')
user.start()
