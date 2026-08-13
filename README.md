Библиотеки
pip install -r requirements.txt

Миграции
python manage.py migrate

Добавить категории 
python manage.py shell


>>> from store.models import Category
>>> Category.objects.create(name="Одежда",description="Категория одежды")
<Category: Одежда>


>>> exit()


Старт
python manage.py runserver

