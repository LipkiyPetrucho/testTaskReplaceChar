import os
import sys


def read_config(file_name):
    """
         Функция, которая читает файл конфигурации и
         преобразует все его символы в ключи и значения словаря.
     """
    # проверяем, существует ли файл
    if not os.path.exists(file_name):
        print(f'Файл {file_name} не найден.')
        exit(1)

    # проверяем доступен ли файл для чтения и содержит ли допустимые данные
    try:
        # with - контекстный менеджер. С помощью него открываем, читаем, закрываем файл.
        with open(file_name, 'r') as file:
            """
                1. проходим циклом по всем текстовым строчкам в файле.
                2. методом strip() убираем из каждой текстовой строчки все интервалы
                (пробелы, табуляция, символы пустых строк) вначале и в конце.
                3. метод split() разбиваем каждую текстовую строчку файла на части
                в виде строк в том месте где есть разделительный символ '=' каждая часть
                становится элементом списка. Список преобразуем в словарь.
            """
            return dict(line.strip().split('=') for line in file)
    except Exception as e:
        print(f'Произошла ошибка при чтении файла {file_name}: {str(e)}')
        exit(1)


def process_text(file_name, config):
    """
        Функция, которая преобразует текст файла по словарю из файла конфигурации.
    """
    if not os.path.exists(file_name):
        print(f"Файл {file_name} не найден.")
        exit(1)

    try:
        # Открываем текстовый файл
        with open(file_name, 'r') as file:
            # Создаём список, добавляя в него элементы в виде строк,
            # которые мы получаем из текстовых строчек текстового файла.
            # Присваиваем списку имя переменной.
            lines = [line.strip() for line in file]

            # Проверяем, пустой ли список строк
            if not lines:
                print(f"**Предупреждение:** Текстовый файл {file_name} содержит только пустые строки.")
                exit(1)

    except Exception as e:
        print(f"Произошла ошибка при чтении файла {file_name}: {str(e)}")
        exit(1)

    # Подсчитываем количество замен для каждого ключа.
    replacements = []
    for key, value in config.items():
        count = sum(line.count(key) for line in lines)
        replacements.append((key, value, count))

        # Замена
        lines = [line.replace(key, value) for line in lines]

    # Сортировка
    lines.sort(key=lambda line: sum(line.count(rep[1]) for rep in replacements), reverse=True)

    results = '\n'.join(lines)
    return results


def main(config_file, text_file):
    """Главная функция которая запускает другие функции"""
    config = read_config(config_file)
    results = process_text(text_file, config)

    print(results)


# Вызываем main с аргументами, полученными из командной строки
# sys.argv[1] - путь к файлу конфигурации.
# sys.argv[2] - путь к текстовому файлу.
if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
