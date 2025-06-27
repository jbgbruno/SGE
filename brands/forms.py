from django import forms
from . import models


class BrandForm(forms.ModelForm):
    class Meta:
        model = models.Brand
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nome da marca',
                    'aria-label': 'Nome da marca',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 3,
                    'placeholder': 'Descrição da marca',
                    'aria-label': 'Descrição da marca',
                }
            ),
        }
        labels = {
            'name': 'Nome',
            'description': 'Descrição',
        }
