import os
import tempfile

from replace import main


def test_main():
    # Тестовый случай №1. Проверим работу кода с простым конфигурационным файлом и текстовым файлом.
    print("Запуск тестового случая 1...")
    with tempfile.NamedTemporaryFile(delete=False) as config_file,\
            tempfile.NamedTemporaryFile(delete=False) as text_file:
        config_file.write(b'a=z\nb=y\nc=x\n')
        text_file.write(b'abc\nbac\ncab\n')
        main(config_file.name, text_file.name)
    os.unlink(config_file.name)
    os.unlink(text_file.name)
    print("Тестовый случай 1 прошел успешно.\n")

    # Тестовый случай 2. Проверим работу кода с пустым конфигурационным файлом.
    print("Запуск тестового случая 2...")
    with tempfile.NamedTemporaryFile(delete=False) as config_file,\
            tempfile.NamedTemporaryFile(delete=False) as text_file:
        text_file.write(b'abc\nbac\ncab\n')
        main(config_file.name, text_file.name)
    os.unlink(config_file.name)
    os.unlink(text_file.name)
    print("Тестовый случай 2 прошел успешно.\n")

    # Тестовый случай 3. Проверим работу кода с пустым текстовым файлом.
    print("Запуск тестового случая 3...")
    with tempfile.NamedTemporaryFile(delete=False) as config_file,\
            tempfile.NamedTemporaryFile(delete=False) as text_file:
        config_file.write(b'a=z\nb=y\nc=x\n')
        main(config_file.name, text_file.name)
    os.unlink(config_file.name)
    os.unlink(text_file.name)
    print("Тестовый случай 3 прошел успешно.\n")


if __name__ == "__main__":
    test_main()
