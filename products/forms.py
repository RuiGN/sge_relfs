from django import forms
from . import models


class ProductForm(forms.ModelForm):

    class Meta:
        model = models.Product
        fields = ['title', 'category', 'brand', 'description', 'serie_number', 'cost_price', 'cash_selling_price', 'selling_price', 'photo']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'brand': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'serie_number': forms.TextInput(attrs={'class': 'form-control'}),
            'cost_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'cash_selling_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'selling_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Título',
            'category': 'Categoria',
            'brand': 'Marca',
            'description': 'Descrição',
            'serie_number': 'Número de Série',
            'cost_price': 'Preço de Custo',
            'cash_selling_price': 'Preço à Vista',
            'selling_price': 'Preço a Prazo',
            'photo': 'Imagem',
        }
