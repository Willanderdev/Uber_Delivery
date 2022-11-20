from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .forms import Formendereço
from django.contrib import messages
from .models import Servicos
from .coordenadas import coord, distancia, valor, Servidor, momento


def Index(request):
    if str(request.method) == 'POST':
        form = Formendereço(request.POST, request.FILES)
        if form.is_valid():
            # form.save()
            context = {
                'form': form
            }

            list1 = []
            coleta = context['form']['coleta'].value()
            entrega = context['form']['entrega'].value()
            veiculo = context['form']['veiculo'].value()
            list1.append(coleta)
            list1.append(entrega)

            coordenadas = []

            for i in range(len(list1)):
                
                c = coord(list1[i-1])
                coordenadas.append(c)
            dist = distancia(coordenadas)
            value = valor(dist, veiculo)

            # salvando dados acrescentando distancia no bd Servicos.
            b = Servicos(servicos=context['form']['servicos'].value(), coleta=context['form']['coleta'].value(
            ), entrega=context['form']['entrega'].value(), time=momento(), veiculo=context['form']['veiculo'].value(), distancia=dist, valor=value, status='Pending')
            
            b.save()

            return redirect('servicos')

        else:
            print('erro')
            messages.success(request, 'erro')

    return render(request, 'index.html')


def Servico(request):
    corrida = Servicos.objects.all()
    corrida = corrida[len(corrida)-1]

    context = {
        'servicos': corrida.servicos,
        'coleta': corrida.coleta,
        'entrega': corrida.entrega,
        'veiculo': corrida.veiculo,
        'distancia': corrida.distancia,
        'valor': corrida.valor
    }
    if request.method == 'POST':
        return redirect('solicite')
        
    return render(request, 'servicos.html', context)


def Solicite(request):
    # if request.method == 'POST':
    #     Servidor()
    return render(request, 'solicite.html')


def Profile(request):
    form = Formendereço()

    context = {
        'servicos': Servicos.objects.all(),
        'total': Servicos.objects.all().count(),
        'pending':  Servicos.objects.all().filter(status='Pending')
    }

    return render(request, 'profile.html', context)


def Editar(request, id):
    servico = get_object_or_404(Servicos, pk=id)
    form = Formendereço(instance=servico)

    if (request.method == 'POST'):
        form = Formendereço(request.POST, instance=servico)
        if (form.is_valid()):
            servico.save()
            return redirect('profile')
    else:
        return render(request, 'update.html', {"servico": servico, "form": form})


def Delete(request, id):
    produto = get_object_or_404(Servicos, pk=id)
    produto.delete()
    return redirect('profile')





