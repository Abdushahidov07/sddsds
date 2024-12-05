import time
import os

# Путь к файлу программы
file_path = 'auto_update_program.py'

# Список команд для выполнения
commands = [
    "",
    "echo 'Second Command'",
    "echo 'Third Command'"
]

# Индекс текущей команды
command_index = 0

# Счётчик для добавления текста в код
counter = 1

def execute_commands():
    global command_index
    
    # Выполняем три команды
    for _ in range(3):
        current_command = commands[command_index]
        os.system(current_command)
        
        # Переходим к следующей команде (по кругу)
        command_index = (command_index + 1) % len(commands)
    
    # После выполнения трех команд обновляем код
    update_code()

def update_code():
    global counter
    
    # Чтение текущего кода программы
    with open(file_path, 'r') as file:
        code = file.read()
    
    # Текст, который мы будем добавлять в код
    new_code = f"\n# Добавление новой строки в код: {counter}"
    
    # Обновление кода программы
    code += new_code
    
    # Запись обновленного кода обратно в файл
    with open(file_path, 'w') as file:
        file.write(code)
    
    print(f"Код обновлен, добавлена строка: {new_code}")
    
    # Увеличиваем счетчик для следующего изменения
    counter += 1
    
    # Задержка 2 секунды перед следующим циклом
    time.sleep(2)

    # После обновления кода, выполняем следующий цикл
    execute_commands()

# Запуск программы
execute_commands()