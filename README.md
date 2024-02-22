# Django Clothing Store

Этот проект на Django представляет собой онлайн-магазин одежды. Проект использует фреймворк Django и включает простой
каталог товаров с категориями, подробной информацией о товарах и аутентификацией пользователей.

## Начало работы

- Создать проект
- Создать виртуальную среду:

```
python -m venv venv
```

- Активация виртуальной среды:

```
На Windows:
venv\Scripts\activate
```

```
На macOS и Linux:
source venv/bin/activate
```

### Библиотеки

- Python 3.11
- Django==5.0.1
- pillow10.2.0

### Установите зависимости:

```
 pip install -r requirements.txt
```

### Настройка базы данных

Применить миграции:
```
./manage.py migrate
```

Создание суперпользователя для доступа к админ-панели:

```
./manage.py createsuperuser
```

### Запуск сервера разработки

Запуск сервер разработки Django:

```
./manage.py runserver
```

### Запуск PostgresSQL

Загрузка библиотек:
```
psycopg2-binary==2.9.9
psycopg2==2.9.9
python-decouple==3.8 - для шифровки данных(.env)
```
Создать файлы:
```
Dockerfile
docker-compose.yml
```


### Информация по командам для проекта

```
./manage.py runserver запуск сервера
./manage.py. startapp products - создание папки templates
./manage.py makemigrations - создание миграции
./manage.py migrate - применение миграций
./manage.py createsuperuser - создание супер юзера
./manage.py startapp users - создание приложения для авторизации
docker-compose exec web python manage.py test - запуск теста с db Docker
```

Добавление объекта через python Console:

```
from products.models import ProductCategory
category = ProductCategory(name='Одежда', description='Описание для одежды')
ategory.save()
```

Django Fixtures

```
./manage.py dumpdata products.ProductCategory -o categories.json - дамп таблицы
./manage.py loaddata products/fixtures/goods.json - установка фикстур
```
