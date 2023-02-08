from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .forms import Formendereço, Formsolicitação
from django.contrib import messages
from .models import Servicos, Sol_Servicos
from .coordenadas import coord, distancia, valor, Servidor, momento, decimalconverter
from django.contrib.auth.models import User, Group
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required


@login_required(login_url='usuarios/login/')
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
            ), entrega=context['form']['entrega'].value(), time=momento(), veiculo=context['form']['veiculo'].value(), distancia=dist, valor=value, status='Waiting')

            b.save()

            return redirect('servicos')

        else:
            print('erro')
            messages.success(request, 'erro')

    return render(request, 'index.html')


@login_required(login_url='usuarios/login/')
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

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':

        coleta = request.POST.get("coleta2")
        entrega = request.POST.get("entrega2")
        veiculo = request.POST.get("veiculo2")

        distancia = request.POST.get("valor_distancia")

        distancia2 = decimalconverter(distancia)

        valor = request.POST.get("valor")
        valor2 = decimalconverter(valor)

        b = Sol_Servicos(servicos=corrida.servicos, coleta=coleta, entrega=entrega, time=momento(
        ), veiculo=veiculo, distancia=distancia2, valor=valor2, status='Pending')

        b.save()
        return JsonResponse({"message": "success"})
        # return redirect('Solicite')

    return render(request, 'servicos.html', context)


class Solicite(TemplateView):

    template_name = 'solicite.html'
