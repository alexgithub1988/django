import pytest
from django.core.exceptions import ValidationError
from store.forms import ProductForm
from store.models import Product, Category


@pytest.mark.django_db
def test_product_form_valid():
    """Корректная форма проходит валидацию"""
    cat = Category.objects.create(name="Тестовая категория")
    form = ProductForm(data={
        'name': 'Тестовый товар',
        'description': 'Описание товара',
        'price': '500.00',
        'category': cat.pk,
    })
    assert form.is_valid()


@pytest.mark.django_db
def test_product_form_negative_price():
    """Отрицательная цена не проходит"""
    cat = Category.objects.create(name="Тестовая категория")
    form = ProductForm(data={
        'name': 'Тестовый товар',
        'description': 'Описание',
        'price': '-100.00',
        'category': cat.pk,
    })
    assert form.is_valid() is False
    assert 'price' in form.errors
    assert 'Цена не может быть меньше или равной 0' in form.errors['price']


@pytest.mark.django_db
def test_product_form_empty_name():
    """Пустое название не проходит валидацию"""
    cat = Category.objects.create(name="Тестовая категория")
    form = ProductForm(data={
        'name': '',
        'description': 'Описание',
        'price': '100.00',
        'category': cat.pk,
    })
    assert form.is_valid() is False
    assert 'name' in form.errors


@pytest.mark.django_db
def test_product_form_zero_price():
    """Цена 0 проходит не проходит валидацию"""
    cat = Category.objects.create(name="Тестовая категория")
    form = ProductForm(data={
        'name': 'Бесплатный товар',
        'description': 'Раздача',
        'price': '0.00',
        'category': cat.pk,
    })
    assert form.is_valid() is False
    assert 'price' in form.errors
    assert 'Цена не может быть меньше или равной 0' in form.errors['price']

