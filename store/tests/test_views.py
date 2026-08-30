import pytest
from django.urls import reverse
from store.models import Product


@pytest.mark.django_db
def test_product_detail_404(client):
    """Детальная страница несуществующего товара — 404"""
    url = reverse('product_detail', kwargs={'pk': 99999})
    response = client.get(url)
    assert response.status_code == 404


@pytest.mark.django_db
def test_product_create_view_get(client):
    """GET создания товара — возвращает форму"""
    url = reverse('product_create')
    response = client.get(url)
    assert response.status_code == 200
    assert 'form' in response.context


@pytest.mark.django_db
def test_product_create_view_post(client, category):
    """POST создания товара — создаёт и редиректит"""
    url = reverse('product_create')
    data = {
        'name': 'Новый товар',
        'description': 'Описание',
        'price': '499.99',
        'category': category.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302
    assert Product.objects.filter(name='Новый товар').exists()


@pytest.mark.django_db
def test_product_update_view_get(client, product):
    """GET обновления товара — возвращает форму"""
    url = reverse('product_update', kwargs={'pk': product.pk})
    response = client.get(url)
    assert response.status_code == 200
    assert 'form' in response.context


@pytest.mark.django_db
def test_product_update_view_post(client, product):
    """POST обновления товара — обновляет и редиректит"""
    url = reverse('product_update', kwargs={'pk': product.pk})
    data = {
        'name': 'Обновлённый товар',
        'description': 'Новое описание',
        'price': '999.99',
        'category': product.category.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302
    product.refresh_from_db()
    assert product.name == 'Обновлённый товар'
    assert str(product.price) == '999.99'


@pytest.mark.django_db
def test_product_update_view_404(client):
    """Обновление несуществующего товара — 404"""
    url = reverse('product_update', kwargs={'pk': 99999})
    response = client.get(url)
    assert response.status_code == 404


@pytest.mark.django_db
def test_product_delete_view_post(client, product):
    """POST удаления товара — удаляет и редиректит"""
    url = reverse('product_delete', kwargs={'pk': product.pk})
    response = client.post(url)
    assert response.status_code == 302
    assert not Product.objects.filter(pk=product.pk).exists()


