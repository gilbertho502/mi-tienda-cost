from django import forms

class FormularioContacto(forms.Form):
    nombre = forms.CharField(label='Nombre', required=True, max_length=50)
    email = forms.CharField(label='Email', required=True)
    Asunto = forms.CharField(label='Asunto', required=True)
    contenido = forms.CharField(label='Contenido', widget=forms.Textarea, required=False)