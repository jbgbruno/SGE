from django import forms
from . import models


class CategoryForm(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nome da categoria',
                    'aria-label': 'Nome da categoria',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 3,
                    'placeholder': 'Descrição da categoria',
                    'aria-label': 'Descrição da categoria',
                }
            ),
        }
        labels = {
            'name': 'Nome',
            'description': 'Descrição',
        }
