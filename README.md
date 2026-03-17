# Playwright Automation Project (UI Testing)

Учебный проект по автоматизации тестирования пользовательского интерфейса (UI) с использованием современного стека на Python. Проект построен с соблюдением паттерна **Page Object Model (POM)** и принципов чистой архитектуры.

## 🌐 Сайт тестирования

https://www.qa-practice.com/

## 🛠 Технологический стек

* **Язык:** Python 3.13.12
* **Фреймворк для тестов:** Pytest
* **Инструмент автоматизации:** Playwright (Sync API)
* **Управление конфигурацией:** python-dotenv (хранение URL и секретов в .env)
* **Стандарты кода:** Type Hinting, PEP8

## 📂 Структура проекта

```text
├── pages/                  # Слой страниц (Page Object Model)
│   ├── base_page.py        # Базовый класс с общими методами
│   ├── locators.py         # Централизованное хранение локаторов
│   └── ..._page.py         # Логика конкретных страниц
├── tests/                  # Тестовые сценарии
├── .env.example            # Шаблон конфигурационных данных
├── conftest.py             # Фикстуры Pytest (инициализация браузера и страниц)
├── pytest.ini              # Настройки Pytest и маркировка тестов
└── requirements.txt        # Список зависимостей
```

## 🚀 Как запустить проект
Клонируйте репозиторий:

```Bash
git clone [https://github.com/ВАШ_ЛОГИН/ВАШ_РЕПОЗИТОРИЙ.git](https://github.com/ВАШ_ЛОГИН/ВАШ_РЕПОЗИТОРИЙ.git)
cd playwright-pytest-study
```

Создайте и активируйте виртуальное окружение:

```Bash
python -m venv venv
source venv/bin/activate  # Для Linux/macOS
# или
venv\Scripts\activate     # Для Windows
```

Установите зависимости:

```Bash
pip install -r requirements.txt
playwright install
```

Настройте окружение:
Создайте файл .env на основе .env.example и укажите актуальные URL.

Запустите тесты:

```Bash
pytest
```
