./manage.py runserver запуск сервера
./manage.py. startapp products - создание папки templates
./manage.py makemigrations - создание миграции
./manage.py migrate - применение миграций
./manage.py createsuperuser - создание супер юзера

Добавление объекта через python Console:
from products.models import ProductCategory
category = ProductCategory(name='Одежда', description='Описание для одежды')
ategory.save()

Django Fixtures
./manage.py dumpdata products.ProductCategory -o categories.json - дамп таблицы
 ./manage.py loaddata products/fixtures/goods.json - установка фикстур

 ./manage.py startapp users - создание приложения для авторизации