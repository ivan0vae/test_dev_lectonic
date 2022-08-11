# test_dev_lectonic
Как запустить тесты
1.	Скачать driver for Chrome https://chromedriver.chromium.org/downloads и вставить в строку вместо … адрес нахождения драйвера на компьютере 
driver = webdriver.Chrome(‘…’)
2.	Установить библиотеки:
-time
-selenium
-json
3. Запуск теста либо с помощью python -m pytest -v --driver Chrome --driver-path …  название теста.ру (вместо … адрес нахождения драйвера на компьютере), 
либо кликнув на run test (зеленый треугольник) рядом с def

Примечание:
!!! Тесты необходимо выполнять строго в приведенной ниже последовательности !!!

- первый тест – это test_selenium_lect_mainpage – проверяем возможность регистрации нового пользователя (необходимо ввести почту). 
После этого на указанную почту приходит ссылка для дальнейшей регистрации

- полученную из письма ссылку необходимо вставить в строку driver.get(‘https…’) второго теста test_selenium_inputpass. 
Этим тестом мы проверяется возможность установки пароля нового пользователя. После успешного завершения теста происходит переход на страницу заполнения базового профиля.

- для того чтобы не выходить из системы при осуществлении последующих тестов, необходимо провести тест на авторизацию с сохранением cookie (test_selenium_auth)

- далее протестируем возможность создания базового профиля пользователя (test_selenium_createprofile). После успешного прохождения теста 
открывается возможность выбора роли пользователя (лектор или заказчик)
- следующим тестом проверяем возможность выбора роли пользователя (лектор или заказчик) и тестируем возможность указания доп информации (test_selenium_add_role). 
После успешного прохождения данного теста попадаем в кабинет лектора.

