import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_index_view(client):
  """Тест проверки главной страницы"""
  url = reverse('product_list')
  response = client.get(url)
  assert response.status_code  == 200
  assert "Список товаров" in response.content.decode()


@pytest.mark.django_db
def test_product_list_empty(client):
    """Список товаров — пустой список"""
    url = reverse('product_list')
    response = client.get(url)
    assert response.status_code == 200
    assert 'Товаров пока нет' in response.content.decode()


@pytest.mark.django_db
def test_product_list_with_products(client, product):
    """Список товаров — карточки и ссылки"""
    url = reverse('product_list')
    response = client.get(url)
    content = response.content.decode()
    assert product.name in content
    assert 'Подробнее' in content
    assert 'Редактировать' in content


@pytest.mark.django_db
def test_messages_after_delete(client, product):
    """После удаления отображается сообщение"""
    url = reverse('product_delete', kwargs={'pk': product.pk})
    response = client.post(url)
    assert response.status_code == 302
    response = client.get(reverse('product_list'))
    assert 'удален' in response.content.decode()


@pytest.mark.django_db
def test_product_confirm_delete_page(client, product):
    """Страница подтверждения удаления — содержит форму"""
    url = reverse('product_delete', kwargs={'pk': product.pk})
    response = client.get(url)
    assert response.status_code == 200
    content = response.content.decode()
    assert product.name in content
    assert 'Подтвердите удаление' in content


