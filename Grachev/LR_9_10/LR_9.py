from prettytable import PrettyTable
import re


class Database(object):
    """Класса для работы сс импровизированной базой данных"""

    def writing_data_to_file(self, data):
        """Функция для построчной записи данных в файл"""
        try:
            with open('Database.db', 'a', encoding='UTF-8') as db:
                line = str('|'.join(data)), '\n'
                db.writelines(line)
                db.close()
        except:
            print("Произошла ошибка при работе с базой Database.db!")
        finally:
            if db is not None:
                db.close()

    def reading_data_from_file(self):
        """Функция чтения данных из файла"""
        try:
            with open('Database.db', 'r', encoding='UTF-8') as db:
                lines = db.read().splitlines()
                db.close()
            return lines
        except:
            print("Произошла ошибка при работе с базой Database.db!")
        finally:
            if db is not None:
                db.close()

    def search_by_model(self):
        """Функция поиска данных по модели"""
        constant = input('Укажите что ищем: ')
        lines = Database().reading_data_from_file()
        td = []
        for i in lines[1:]:
            td_data = (''.join(i)).split('|')
            res = re.findall(constant.upper(), td_data[0].upper())
            if len(res) > 0:
                td.append(i)
        if len(td) > 0:
            res_list = [lines[0], *td]
            return res_list
        else:
            print('Данные не найдены!')
            a = input('Введите 1 для повтороного поиска, любую клавишу для возврата в главное меню: ')
            if a == '1':
                self.search_by_model()
            else:
                main()

    def search_by_type(self):
        """Функция поиска данных по типу"""
        constant = input('Укажите что ищем: ')
        lines = Database().reading_data_from_file()
        td = []
        for i in lines[1:]:
            td_data = (''.join(i)).split('|')
            res = re.findall(constant.upper(), td_data[1].upper())
            if len(res) > 0:
                td.append(i)
        if len(td) > 0:
            res_list = [lines[0], *td]
            return res_list
        else:
            print('Данные не найдены!')
            a = input('Введите 1 для повтороного поиска, любую клавишу для возврата в главное меню: ')
            if a == '1':
                self.search_by_type()
            else:
                main()

    def search_by_start_date(self):
        """Функция поиска данных по дате начала выпуска"""
        constant = input('Укажите что ищем: ')
        lines = Database().reading_data_from_file()
        td = []
        for i in lines[1:]:
            td_data = (''.join(i)).split('|')
            res = re.findall(constant.upper(), td_data[2].upper())
            if len(res) > 0:
                td.append(i)
        if len(td) > 0:
            res_list = [lines[0], *td]
            return res_list
        else:
            print('Данные не найдены!')
            a = input('Введите 1 для повтороного поиска, любую клавишу для возврата в главное меню: ')
            if a == '1':
                self.search_by_start_date()
            else:
                main()

    def search_by_end_date(self):
        """Функция поиска данных по дате конца выпуска"""
        constant = input('Укажите что ищем: ')
        lines = Database().reading_data_from_file()
        td = []
        for i in lines[1:]:
            td_data = (''.join(i)).split('|')
            res = re.findall(constant.upper(), td_data[3].upper())
            if len(res) > 0:
                td.append(i)
        if len(td) > 0:
            res_list = [lines[0], *td]
            return res_list
        else:
            print('Данные не найдены!')
            a = input('Введите 1 для повтороного поиска, любую клавишу для возврата в главное меню: ')
            if a == '1':
                self.search_by_end_date()
            else:
                main()

    def search_by_manufacturer(self):
        """Функция поиска данных по производителю"""
        constant = input('Укажите что ищем: ')
        lines = Database().reading_data_from_file()
        td = []
        for i in lines[1:]:
            td_data = (''.join(i)).split('|')
            res = re.findall(constant.upper(), td_data[4].upper())
            if len(res) > 0:
                td.append(i)
        if len(td) > 0:
            res_list = [lines[0], *td]
            return res_list
        else:
            print('Данные не найдены!')
            a = input('Введите 1 для повтороного поиска, любую клавишу для возврата в главное меню: ')
            if a == '1':
                self.search_by_manufacturer()
            else:
                main()

    def search_all_data(self):
        """Функция поиска данных по всем имеющимся данным"""
        constant = input('Укажите что ищем: ')
        lines = Database().reading_data_from_file()
        td = []
        for i in lines[1:]:
            td_data = (''.join(i)).split('|')
            res = re.findall(constant.upper(), ' '.join(td_data).upper())
            if len(res) > 0:
                td.append(i)
        if len(td) > 0:
            res_list = [lines[0], *td]
            return res_list
        else:
            print('Данные не найдены!')
            a = input('Введите 1 для повтороного поиска, любую клавишу для возврата в главное меню: ')
            if a == '1':
                self.search_all_data()
            else:
                main()


def building_table(lines):
    """Функция построения таблицы и вывода результата пользователю
    Для этого используется библиотека prettytable"""

    th = (''.join(lines[0])).split('|')
    columns = len(th)  # Подсчитаем кол-во столбцов на будущее.
    table = PrettyTable(th)  # Определяем таблицу.
    for i in lines[1:]:
        td_data = (''.join(i)).split('|')
        # Входим в цикл который заполняет нашу таблицу.
        # Цикл будет выполняться до тех пор пока у нас не кончатся данные
        # для заполнения строк таблицы (список td_data).
        while td_data:
            # Используя срез добавляем первые пять элементов в строку.
            # (columns = 5).
            table.add_row(td_data[:columns])
            # Используя срез переопределяем td_data так, чтобы он
            # больше не содержал первых 5 элементов.
            td_data = td_data[columns:]
    print(table)  # Печатаем таблицу


def requesting_data_from_user():
    """Функция для сбора данных у пользователя"""
    def _check_repeat(repeat):
        """Рекурсивная  приватная функция для получения нужного ответа пользователя"""
        repeat = repeat.upper()
        if repeat != 'N' and repeat != 'Y':
            print('Не верный ответ')
            repeat = input('Вы хотите внести новые данные? (Y/n): ')
            _check_repeat(repeat)
        else:
            return repeat

    def _check_answer(answer):
        """Приватная функция замены '' на - """
        if answer == '':
            answer = '-'
        return answer

    name = _check_answer(input('Укажите модель: '))
    name_type = _check_answer(input('Укажите тип: '))
    year = _check_answer(input('Укажите дату начала выпуска: '))
    nothing = _check_answer(input('Укажите дату конца выпуска: '))
    manufacturer = _check_answer(input('Укажите производителя: '))
    repeat = input('Вы хотите внести новые данные? (Y/n): ')
    repeat = _check_repeat(repeat)
    data = [name, name_type, year, nothing, manufacturer]
    Database().writing_data_to_file(data)
    if repeat == 'Y':
        requesting_data_from_user()
    else:
        return


def search_menu():
    """Функция для вывода и обработки поискового меню"""
    def _search_menu_check(arr):
        """Рекурсивная приватная функция для получения нужного ответа пользователя"""
        if arr != '1' and arr != '2' and arr != '3'\
                and arr != '4' and arr != '5' and arr != '6'\
                and arr != '7':
            print('Получены не корректные данные')
            _search_menu_check(arr)
        else:
            return arr
    print('1 - Поиск по моделе\n2 - Поиск по типу\n3 - По дате начала производства\n'
          '4 - По дате конца производства\n5 - Поиск по производителю\n6 - Поиск по всем данным\n'
          '7 - Вернуться в главное меню')
    menu = input('Укажите желаемый пункт меню: ')
    menu = _search_menu_check(menu)
    if menu == '1':
        res_list = Database().search_by_model()
        building_table(res_list)
    elif menu == '2':
        res_list = Database().search_by_type()
        building_table(res_list)
    elif menu == '3':
        res_list = Database().search_by_start_date()
        building_table(res_list)
    elif menu == '4':
        res_list = Database().search_by_end_date()
        building_table(res_list)
    elif menu == '5':
        res_list = Database().search_by_manufacturer()
        building_table(res_list)
    elif menu == '6':
        res_list = Database().search_all_data()
        building_table(res_list)
    elif menu == '7':
        main()


def main():
    """Основаная функция программы"""
    def _check_menu(*args):
        """Приватная рекурсивная функция для обработки полученных данных"""
        menu = input("Введите 1 для добавления данных, 2 для вывода таблицы, 3 для поиска нужных данных: ")
        if menu != '1' and menu != '2' and menu != '3':
            print('Получены не корректные данные')
            _check_menu(menu)
        else:
            return menu

    menu = _check_menu()
    if menu == '1':
        requesting_data_from_user()
        main()
    elif menu == '2':
        lines = Database().reading_data_from_file()
        building_table(lines)
        main()
    elif menu == '3':
        search_menu()
        main()


if __name__ == '__main__':
    main()