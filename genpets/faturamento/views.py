from django.shortcuts import render, redirect,get_object_or_404
from django.db.models import Sum
from .models import Ganho
from ganho.models import Animal
from datetime import datetime

def faturamento(request):
    # Obter o mês e ano atuais
    agora = datetime.now()
    ano_atual = agora.year
    mes_atual = agora.month

    # Lista de meses (para o select)
    MESES = {
        '01': 'Janeiro', '02': 'Fevereiro', '03': 'Março', '04': 'Abril',
        '05': 'Maio', '06': 'Junho', '07': 'Julho', '08': 'Agosto',
        '09': 'Setembro', '10': 'Outubro', '11': 'Novembro', '12': 'Dezembro'
    }

    # Obter mês selecionado no formulário (ou usar o mês atual como padrão)
    mes_selecionado = request.GET.get('mes', f"{mes_atual:02}")

    # Filtrar os ganhos do mês selecionado
    ganhos_filtrados = Ganho.objects.filter(data__month=mes_selecionado, data__year=ano_atual)

    # Calcular o total de faturamento
    total_faturamento = ganhos_filtrados.aggregate(Sum('valor'))['valor__sum'] or 0

    # Calcular ganhos por animal
    ganhos_animais = {}
    for ganho in ganhos_filtrados:
        if ganho.animal not in ganhos_animais:
            ganhos_animais[ganho.animal] = 0
        ganhos_animais[ganho.animal] += ganho.valor

    # Dados para o template
    context = {
        'meses': MESES,  # Dicionário de meses
        'mes_selecionado': MESES[mes_selecionado],  # Nome do mês selecionado
        'total_faturamento': total_faturamento,
        'ganhos_animais': ganhos_animais,
    }

    return render(request, 'faturamento.html', context)


def adicionar_ganho(request):
    if request.method == 'POST':
        animal_id = request.POST['animal']
        valor = request.POST['valor']
        animal = Animal.objects.get(id=animal_id)
        Ganho.objects.create(animal=animal, valor=valor, data=datetime.now())
        return redirect('faturamento')

    # Listar todos os animais cadastrados
    animais = Animal.objects.all()
    return render(request, 'adicionar_ganho.html', {'animais': animais})

