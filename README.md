## Сайт медицинской диагностики

### Используемые технологии

- PostgreSQL
- ORM
- Django
- Bootstrap
- Шаблонизация
- CBV
- Формы
- Аутентификация
- Права доступа

### Описание

На сайте представлены медицинские услуги разделенные по нескольким направлениям.
Для записи на приём к врачу необходимо зарегистрироваться на сайте через почту, а затем выбрать интересующую услугу, выбрать дату и время посещения.

### Эндпоинты:

- Регистрация пользователя
- Просмотр профиля
- Редактирование профиля
- Удаление пользователя
- Список категорий
- Список всех услуг
- Список услуг по категориям
- Список личных записей на приём
- Просмотр личных записей на приём
- Редактирование личных записей на приём
- Удаление личных записей на приём

### Права доступа:
- Анонимный пользователь видит список категорий и услуг но не может записаться на приём к врачу
- Авторизованный пользователь может записаться на приём выбрав услугу дату и время, а также просматривать список личных записей на приём.
