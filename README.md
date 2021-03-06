# Парсер вакансий разработчика

Скрипт предназначен для парсинга сайтов для поиска работы [hh.ru](https://hh.ru/) и [superjob.ru](https://superjob.ru) на наличие вакансий разработчиков разных языков в Москве за последние 30 дней и рассчета средней зп по каждому из них.


## Установка

Для установки зависимостей в командной строке введите:

```
pip install -r requirements.txt
```
Также необходимо зарегистрировать приложение на [SuperJob](https://api.superjob.ru/) и получить его Secret key. Его лучше "спрятать", проэтому в папке со скриптом создаем файл `.env`,
а в него записываем `SUPERJOB_KEY=То что вы получили по инструкции выше`. Например: 
```
SUPERJOB_KEY=v3.r.117263162.22d39dbe074139a3151a2d9524f64cbfd26e5e.8168297fb2dd4bafa54455fbbae29b9c030bafb
``` 

## Запуск

До запуска проргаммы вам необходимо определиться, какой сайт вы собираетесь парсить. Для парсинга [hh.ru](https://hh.ru/) в командной введите(для пользователей Windows):
```
python hh_ru.py
``` 
или (для Linux):
```
python3 hh_ru.py
```
По аналогии, только для [superjob.ru](https://superjob.ru) (для Windows):

```
python superjob.py
``` 
или (для Linux):
```
python3 superjob.py
```
Не торопитесь выключать программу, ей нужно какое-то время, чтобы обработать все вакансии.

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).