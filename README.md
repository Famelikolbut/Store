# Django Clothing Store

Этот  проект на Django представляет собой онлайн-магазин одежды. Проект использует фреймворк Django и включает простой каталог товаров с категориями, подробной информацией о товарах и аутентификацией пользователей.

## Начало работы

1. Создать проект

2. Создать виртуальную среду:
```
python -m venv venv
```

3. Активация виртуальной среды:
```
На Windows:
venv\Scripts\activate
```
```
На macOS и Linux:
source venv/bin/activate
```
### Установка библиотек

- Python 3.11
- pip install Django==5.0.1
- pip install pillow==10.2.0

### Установите зависимости:

```
    pip install -r requirements.txt
```

### Настройка базы данных

Создайте суперпользователя для доступа к админ-панели:

```
   ./manage.py createsuperuser
```

### Запуск сервера разработки

Запустите сервер разработки Django:

```
   ./manage.py runserver
```


### Информация по командам для проекта 
```
./manage.py runserver запуск сервера
./manage.py. startapp products - создание папки templates
./manage.py makemigrations - создание миграции
./manage.py migrate - применение миграций
./manage.py createsuperuser - создание супер юзера
./manage.py startapp users - создание приложения для авторизации
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
