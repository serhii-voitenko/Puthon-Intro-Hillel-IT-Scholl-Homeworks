import random
import zipfile


def hack_archive(file_name):
    PASSWORD_LENGTH = 4
    """
    Функция брутфорсит запароленный архив
    """
    file_to_open = zipfile.ZipFile(file_name)  # объект архива
    wrong_passwords = []  # список паролей, которые не подошли
    tries = 0  # колличество неудачных попыток

    while True:
        def extract_archive(file_to_open, password):
            """
            Функция открывает архив с паролем и возвращает результат операции (bool)
            """
            try:
                file_to_open.extractall(pwd=password.encode())
                return True
            except Exception as e:
                print(e)
                return False

        chars = '1234567890'
        password = ''
        for i in range(PASSWORD_LENGTH):
            password += random.choice(chars)
            if password in wrong_passwords:
                continue
        if extract_archive(file_to_open, password):
            break
        tries += 1
        wrong_passwords.append(password)

    print(f'Archive {file_name} is hacked. Password - {password}')
    print(f'Password was found after {tries} tries')


#############
filename = 'hack.zip'
hack_archive(filename)
