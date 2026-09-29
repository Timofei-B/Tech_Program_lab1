import platform
import os
import socket
import sys
import json

# Определяем ОС одним словом
system = platform.system()
name = {
    "Linux": "Linux",
    "Windows": "Windows",
    "Darwin": "MacOS",
    }.get(system, system)  # если система другая — оставим как есть
data = {
    # Общее
    "Имя компьютера": socket.gethostname(),
    "Операционная система": name,
    "Релиз ОС": platform.release(),
    "Версия ОС": platform.version(),
    "Архитектура": platform.machine(),
    "Процессор": platform.processor(),
    "Платформа": platform.platform(),
    "Количество ядер CPU": os.cpu_count(),
    # Детали ОС — берём первое доступное значение через or
    "Детали ОС": (
        platform.win32_ver()  # Windows
        or platform.libc_ver()      # Linux
        or platform.mac_ver()    # macOS
    ),
    # Переменные окружения — тоже через or (работает на всех ОС)
    "Оболочка командной строки": (
        os.environ.get('SHELL')    # Linux / macOS
        or os.environ.get('COMSPEC')  # Windows
    ),
    "Имя пользователя": (
        os.environ.get('USER')      # Linux / macOS
        or os.environ.get('USERNAME')  # Windows
    ),
    "Путь к домашней папке пользователя": (
        os.environ.get('HOME')          # Linux / macOS
        or os.environ.get('USERPROFILE')  # Windows
    ),
    # Python
    "Версия Python": sys.version,
    "Версия Python (кратко)": platform.python_version(),
    "Компилятор Python": platform.python_compiler(),
    "Реализация Python": platform.python_implementation(),
    "Путь к Python": sys.executable,
    # Рабочая папка
    "Текущая папка": os.getcwd(),
}


with open("os_info.json", "w", encoding="utf-8") as файл:
    json.dump(data, файл, indent=4, ensure_ascii=False)
print(f"Информация сохранена в файл: os_info.json") 