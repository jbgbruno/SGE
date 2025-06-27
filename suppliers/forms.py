from django import forms
from . import models


class SupplierForm(forms.ModelForm):
    class Meta:
        model = models.Supplier
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nome do Fornecedor',
                    'aria-label': 'Nome do Fornecedor',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 3,
                    'placeholder': 'Descrição do Fornecedor',
                    'aria-label': 'Descrição do Fornecedor',
                }
            ),
        }
        labels = {
            'name': 'Nome',
            'description': 'Descrição',
        }
