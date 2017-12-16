from django import forms

#formulario para los mensajes
class MensajeForm(forms.Form):
    texto = forms.CharField(required=False,label='', max_length=10000, widget=forms.TextInput(attrs={"placeholder":"escribe un mensaje","class":"col s11"}))
    file = forms.FileField(label=" ",required=False)