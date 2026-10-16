Parabank UI Tests

Проект UI-автотестов для страницы регистрации интернет-банка
Parabank (https://parabank.parasoft.com/) на Python + Selenium + Pytest + Allure.

Описание

Проект реализует архитектуру Page Object Model (POM) и проверяет сценарий
регистрации нового пользователя:

1 позитивный тест успешная регистрация;
5 негативных тестов пустые обязательные поля, несовпадение паролей и др.

Тесты поддерживают мультибраузерность Chrome, Firefox, строят Allure-отчёт
и при падении теста автоматически прикладывают:
скриншот экрана;
логи браузера (console log);
сетевые запросы (performance log).

Стек технологий

| Технология         | Назначение                              |
|--------------------|-----------------------------------------|
| Python 3.10+       | язык написания тестов                   |
| Selenium 4         | управление браузером                    |
| Pytest             | фреймворк для запуска тестов            |
| Allure             | отчётность                              |
| webdriver-manager  | автоматическая установка драйверов      |

Структура проекта

parabank-ui-tests/
├── pages/                           Page Object Model
│   ├── __init__.py
│   ├── base_page.py                 Базовый класс страницы
│   └── registration_page.py         Страница регистрации
├── tests/
│   ├── __init__.py
│   └── test_registration.py         Тесты регистрации
├── utils/
│   ├── __init__.py
│   └── attach.py                    Прикладывание артефактов в Allure
├── conftest.py                      Фикстуры: driver, base_url, хуки
├── pytest.ini                       Настройки Pytest
├── requirements.txt                 Зависимости
├── .gitignore
└── README.md

Установка

1. Клонировать репозиторий:

   git clone https://github.com/<ваш_логин>/parabank-ui-tests.git
   cd parabank-ui-tests

2. Создать и активировать виртуальное окружение:

   python -m venv venv

    Windows
   venv\Scripts\activate

    Linux / macOS
   source venv/bin/activate

3. Установить зависимости:

   pip install -r requirements.txt

4. Установить Allure CLI (требуется Java 8+):

   Скачать: https://github.com/allure-framework/allure2/releases
   Распаковать и добавить bin в PATH.

Запуск тестов

Запуск в Chrome

pytest --browser=chrome

Запуск в Firefox

pytest --browser=firefox

Запуск только позитивных тестов

pytest -m positive

Запуск только негативных тестов

pytest -m negative

Запуск всех тестов с генерацией Allure-результатов

pytest --alluredir=allure-results --clean-alluredir

Allure-отчёт

Открыть отчёт в браузере:

allure serve allure-results

Сгенерировать статический отчёт:

allure generate allure-results -o allure-report --clean
allure open allure-report

В отчёте для каждого теста будут:

шаги с декораторами @allure.step;
вложения (скриншот, логи браузера, сетевые запросы) при падении;
разметка feature / story / severity / title.

Что проверяется

Позитивный сценарий

| № | Название теста                         | Что проверяем                                                              |
|---|----------------------------------------|----------------------------------------------------------------------------|
| 1 | Успешная регистрация нового пользователя | Заполнение всей формы валидными данными, переход на страницу приветствия |

Негативные сценарии

| № | Название теста                          | Что проверяем                                  |
|---|-----------------------------------------|------------------------------------------------|
| 2 | Регистрация с пустым Username           | Сообщение «Username is required»               |
| 3 | Регистрация с пустым паролем            | Сообщение «Password is required»               |
| 4 | Пароль и подтверждение не совпадают     | Сообщение «Passwords did not match»            |
| 5 | Регистрация с пустым First Name         | Сообщение «First name is required»             |
| 6 | Регистрация с пустым SSN                | Сообщение «Social Security Number is required» |

Архитектура

BasePage — низкоуровневые действия: open, find, click, type,
  get_text, is_visible. Обёрнут allure-шагами.
RegistrationPage — наследник BasePage, содержит локаторы и методы
  заполнения формы. Все методы возвращают self (Цепочка вызовов).
conftest.py:
driver — фикстура с параметром --browser, implicitly_wait(0);
base_url — фикстура с URL проекта;
pytest_runtest_makereport — хук, фиксирующий результат каждого этапа теста.
utils/attach.py — функции прикладывания скриншота, логов браузера и
  сетевых запросов в Allure.

Примеры маркеров

@pytest.mark.positive — позитивные тесты;
@pytest.mark.negative — негативные тесты;
@pytest.mark.ui — UI-тесты.

Автор

Богданов Богдан

Лицензия

Проект создан в учебных целях.
