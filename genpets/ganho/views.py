from django.shortcuts import render, redirect
from .models import Animal

def ganho(request):
    animais = Animal.objects.all()
    return render(request, 'ganho.html', {'animais': animais})

def cadastrar_animal_view(request):
    return render(request, 'cadastro_ganho.html')

def salvar_animal_view(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        numero = request.POST['numero'].replace('(', '').replace(')', '').replace('-', '').replace(' ', '')  # Remove formatação
        data_nascimento = request.POST['data_nascimento']
        genero = request.POST['genero']
        vacinas = request.POST['vacinas']
        
        # Salvando os dados no banco
        Animal.objects.create(
            nome=nome,
            numero=int(numero),  # Certifica que o número é inteiro
            data_nascimento=data_nascimento,
            genero=genero,
            vacinas=vacinas
        )
        return redirect('ganho')
