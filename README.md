Проверка аутентификации и авторизации пользователя
Описание теста:
Цель: Проверка возможности входа зарегистрированного пользователя
Шаги:
1. Открыть страницу логина
2. Ввести в поле username логин standard_user
3. Ввести в поле password пароль secret_sauce
4. Нажать кнопку Login
5. Ожидаемый результат: Открыта страница с товарами, пользователь видит таблицу
с товарами

Для проверки необходимо, чтобы был установлен python в вашей системе, также pytest и selenium. Для установки pytest и selenium, необходимо ввести следующие команды через терминал python, либо командную строку:
pip install pytest
pip install selenium

Чтобы запустить два теста нужно ввести следующую команду в терминале:
pytest -v

Для получения отчета allure, нужно установить Allure Report, и установить allure для pytest через терминал с помощью следующей команды:
pip install allure-pytest

Для запуска теста с формированием allure отчета нужно ввести следующую команду, после которой также создаться папка, где будут хранится файлы json:
pytest -v --alluredir allure_reports

Сам отчет необходимо собрать с помощью команды:
allure serve allure_reports

В ходе теста использовались следующие версии:
 python: 3.12.3 
 pytest: 8.3.3
 selenium: 4.26.1
 allure-pytest: 2.13.5
