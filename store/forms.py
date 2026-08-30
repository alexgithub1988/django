from django import forms
from store.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','description','price','category']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'forms-control', 'rows': 4}),
            'price': forms.NumberInput(attrs={'class': 'forms-control', 'step': 0.01}),
            'category': forms.Select(attrs={'class': 'forms-control'})
        }

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price <= 0:
            raise forms.ValidationError("Цена не может быть меньше или равной 0")
        return price
