import pytest

from store.models import Product,Category


@pytest.mark.django_db
def test_create_category(category):
    """Проверяем создание категории"""
    assert Category.objects.count() == 1



@pytest.mark.django_db
def test_create_product(product):
    """Проверяем создание продукта"""
    assert Product.objects.count() == 1

@pytest.mark.django_db
def test_category_str(category):
    """str() категории возвращает name"""
    assert str(category) == category.name


@pytest.mark.django_db
def test_product_str(product):
    """str() продукта возвращает name"""
    assert str(product) == product.name


@pytest.mark.django_db
def test_category_cascade_delete():
    """Удаление категории удаляет привязанные продукты (CASCADE)"""
    cat = Category.objects.create(name="Тестовая категория")
    prod1 = Product.objects.create(name="Продукт 1", price=100, category=cat)
    prod2 = Product.objects.create(name="Продукт 2", price=200, category=cat)
    assert Product.objects.count() == 2
    cat.delete()
    assert Product.objects.count() == 0
    assert Category.objects.count() == 0


