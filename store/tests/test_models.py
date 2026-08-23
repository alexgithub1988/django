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

