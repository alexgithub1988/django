import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_index_view(client):
  """Тест проверки главной страницы"""
  url = reverse('product_list')
  response = client.get(url)
  assert response.status_code  == 200
  assert "Список товаров" in response.content.decode()