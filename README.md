### url_shorter
Маршрутизация
## Описание работы

CRUD операции для работы с маршрутами, test.html - демо основных возможностей,
к сожалению, само построение пришлось оставить в js коде, потому что гугловский js api
возвращает данные немного в дугом формате, чем python библиотека или обращение в API напрямую,
по моим ощущениям эти маршруты лучше, поэтому оставил так.

Документация -- http://127.0.0.1:8000/api/openapi/

## Запуск проекта
 
 env.example -> .env

 ./server/entrypoint.sh -> LF

# Docker

 docker-compose up -d --build

 docker-compose up для запуска основного сервиса
 Миграции прменяются автоматически при запуске контейнера