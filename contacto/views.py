from django.shortcuts import redirect, render
from .forms import FormularioContacto
from django.core.mail import EmailMessage
# Create your views here.

def contacto(request):
    formulario_contacto = FormularioContacto()

    if request.method == 'POST':
        formulario_contacto = FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre = request.POST.get('nombre')
            email = request.POST.get('email')
            asunto = request.POST.get('asunto')
            contenido = request.POST.get('contenido')
            email = EmailMessage(asunto, 'el usuario con nombre {} con direccion {} te escribe lo siguiente: \n\n {}'.format(nombre,email,contenido),'',['vicenteyoc15@gmail.com'], reply_to=[email])

            try:
                email.send()
                return redirect('/contacto/?valido')
            except:
                return redirect('/contacto/?no_valido')   
    return render(request, "contacto/contacto.html", {'miformulario': formulario_contacto})
