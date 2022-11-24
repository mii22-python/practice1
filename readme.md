# Телеграм-бот

## НЕ ВЫКЛАДЫВАЙТЕ ТОКЕН СВОЕГО БОТА!

Запросите бота [@botfather](https://t.me/botfather) о создании бота, сохраните 
токен вашего бота в файле `token` и добавьте имя этого файла в `.gitignore`.

**Ни в коем случае не допускайте отправки токена на GitHub!!!**

При проверке задания преподаватель будет использовать токен своего бота.

## Задание

Напишите Телеграм-бот со следующими командами:

* `/hello` — приветствует пользователя по имени
```
/hello
Привет @User
```
* `/time` — возвращает текущую дату и время в удобном для человека формате
```
/time
Сейчас 15:25, 7 марта 2022 года
```
* `/binom <N> <K>` — вычисляет биномиальный коэффициент для N по K
```
/binom 4 2
Binom(4,2) = 6
```
* `/cat` — показывает картинку случайного кода ошибки HTTP с сайта https://http.cat/

## Начисление баллов

Максимальный балл за выполнение задания: 5 баллов.

1 балл дается если код не работает, но имеет работоспособные фрагменты.

2 балла дается если код работает, но в некоторых случаях дает ошибки.

3 балла дается если код работает без ошибок, но функционал не полностью соответствует заданию.

4 балла дается если код работает и соответствует заданию, но имеет ошибки в оформлении по PEP8.

5 баллов дается если код работает, соответствует заданию и не имеет ошибок по PEP8.

## Документация

* [Telegram Bots](https://core.telegram.org/bots)
* [Библиотека python-telegram-bot](https://python-telegram-bot.readthedocs.io/en/stable/index.html)
* [Клиент HTTP в Python](https://docs.python.org/3/library/http.client.html)
* [Работа с HTTP-запросами в Python](https://docs.python.org/3/library/urllib.request.html)
* [Примеры](https://github.com/python-telegram-bot/python-telegram-bot/tree/v13.14/examples)
* [Что такое биномиальный коэффициент](https://ru.wikipedia.org/wiki/%D0%91%D0%B8%D0%BD%D0%BE%D0%BC%D0%B8%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9_%D0%BA%D0%BE%D1%8D%D1%84%D1%84%D0%B8%D1%86%D0%B8%D0%B5%D0%BD%D1%82)