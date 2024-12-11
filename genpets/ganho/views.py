from django.shortcuts import render, redirect
from .models import Animal

def ganho(request):
    # Captura o termo de busca do parâmetro "q" na URL
    query = request.GET.get('q', '')
    
    # Se houver uma busca, filtra os animais pelo nome usando "icontains"
    if query:
        animais = Animal.objects.filter(nome__icontains=query)
    else:
        # Caso contrário, retorna todos os animais
        animais = Animal.objects.all()

    # Passa os animais e a query atual para o template
    return render(request, 'ganho.html', {'animais': animais, 'query': query})

def cadastrar_animal_view(request):
    # Renderiza a página de cadastro
    return render(request, 'cadastro_ganho.html')

def salvar_animal_view(request):
    if request.method == 'POST':
        # Coleta os dados enviados pelo formulário
        nome = request.POST['nome']
        numero = request.POST['numero'].replace('(', '').replace(')', '').replace('-', '').replace(' ', '')  # Remove formatação
        data_nascimento = request.POST['data_nascimento']
        genero = request.POST['genero']
        vacinas = request.POST['vacinas']

        # Salva os dados no banco de dados
        Animal.objects.create(
            nome=nome,
            numero=int(numero),  # Certifica que o número é inteiro
            data_nascimento=data_nascimento,
            genero=genero,
            vacinas=vacinas
        )
        # Redireciona para a página de ganhos
        return redirect('ganho')
    
    # Caso não seja um POST, redireciona para o formulário de cadastro
    return redirect('cadastrar_animal')
