import os


current_path = 'C:\i\project_9_fishbot'


def flaking(path: str, filename: str) -> None:
    commands = ['black', 'isort', 'flake8']
    if filename.endswith('.py'):
        for comm in commands:
            print(f'{comm} {path}\{filename}')
            os.system(f'{comm} {path}\{filename}')


def scanning(path):
    try:
        for i in os.scandir(path):
            if i.is_dir() and not i.name.startswith('venv'):
                scanning(path + '\\' + i.name)
            if i.is_file() and not i.name.startswith('flaking'):
                flaking(path, i.name)
    except Exception as err:
        return err
    return 'done'


if __name__ == '__main__':
    user_path = input('Введите путь к директории, которую нужно сканировать:')

    print(scanning(user_path))


    # for i in dir(os):
    #      print(i)
    # print(os.listdir())
    # print(*os.walk('.'))

    # for i in os.scandir():
    #     print(i)
    # for i in os.scandir(current_path):
    #     if i.is_dir():
    #         print(current_path + '\\' + i.name)
    #         #scanning(path + '\\' + i.name)
    #     if i.is_file():
    #         print(f'black {current_path}\{i.name}')
    #         #os.system(f'black {path}\{i.name}')


    # print(list(os.scandir())[0].name, list(os.scandir())[0].path)
