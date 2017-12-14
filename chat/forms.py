from django import forms

class MensajeForm(forms.Form):
    texto = forms.CharField(label=None, max_length=10000)
    