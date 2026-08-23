import pytest
from faker import Faker
from faker_ecommerce import EcommerceProvider

from store.models import Product,Category

fake = Faker()
fake.add_provider(EcommerceProvider)




@pytest.fixture
def product(category):
    product_name = fake.product_name()
    price = fake.pydecimal(left_digits=2, right_digits=2, positive=True)
    return Product.objects.create(name=product_name, price=price, category=category)



@pytest.fixture
def category():
    category_name = fake.product_category()
    return Category.objects.create(name=category_name)