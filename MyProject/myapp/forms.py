from django import forms
from django.forms import ModelForm
from myapp.models import *

class RoupaForm(forms.ModelForm):
    class Meta:

        model =  Roupa
        fields = "__all__"
        labels = {
            "titulo": "nome",
            "descricao": "descrição",
            "imagem": "imagem",

        }
        widgets = {
            'titulo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Nome do item",
                }
            ),
            'descricao': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Escreva uma breve descrição",
                }
            ),
            'imagem': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Imagem",
                }
            ),
        }