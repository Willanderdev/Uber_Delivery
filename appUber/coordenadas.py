import requests
import json
import pprint
import socket
# from .models import Servicos
from datetime import datetime


# função que pega as coordenadas baseado no endereço
def coord(endereço):
    list = []
    url = endereço.replace(' ', '%20')
    url = url.replace('-', '%2C')
    url = url.replace(',', '%2C')

    coordenada = f"https://api.geoapify.com/v1/geocode/autocomplete?text={url}&format=json&apiKey=1e424bb14502494792d449fbe3837a97"

    response = requests.get(coordenada)
    response = response.json()
    latitude = response['results'][0]['lat']
    longitude = response['results'][0]['lon']
    
    list.append(longitude)
    list.append(latitude)
    list2 = str(list).replace(' ', '')
    return list2
   
    
   

#função que mede a distancia entre as coordenadas dos dois locais
def distancia(coord):
    url = "https://api.geoapify.com/v1/routematrix?apiKey=1e424bb14502494792d449fbe3837a97"

    headers = {"Content-Type": "application/json"}
    data = '{"mode":"drive","sources":[{"location":'f'{coord[0]}''}],"targets":[{"location":'f'{coord[1]}''}]}'

    try:
        resp = requests.post(url, headers=headers, data=data)
        dist = (resp.json())
        dist = dist['sources_to_targets'][0][0]['distance']
        return dist
        
    except requests.exceptions.HTTPError as e:
        print(e.response.text)
    
    
    

   

#função que retorna o valor do serviço baseado no veículo e distancia
def valor(dist, veiculo):
    if veiculo == 'moto':
        val_km = 8
        valor = val_km*(dist/1000)
        return valor
    elif veiculo == 'carro':
        val_km = 15
        valor = val_km*(dist/1000)
    elif veiculo == 'caminhao':
        val_km = 30
        valor = val_km*(dist/1000)
    else:
        val_km = 50
        valor = val_km*(dist/1000)
    
    return valor



def Servidor():
    HOST = 'localhost'
    PORT = 50000

    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((HOST, PORT))

    servidor.listen()

    print('Aguardando resposta...')
    cliente, ender = servidor.accept()

    print('conectado em', ender)
    
    close = False
    while not close:
        data = cliente.recv(1024).decode('utf-8')
        if data == 'exit':
            close = True
        else:
            print(data)
        cliente.send(input('voçe: ').encode('utf-8'))

    cliente.close()
    servidor.close()


def motorista():
    HOST = 'localhost'
    PORT = 50000

    motorista = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    motorista.connect((HOST, PORT))
    close = False
    while True:
        motorista.send(input('voçe: ').encode('utf-8'))
        data = motorista.recv(1024).decode('utf-8')
        if data == 'exit':
            close = True
            
        else:
            print(data)
            
    motorista.close()


# corrida = list(Servicos.objects.all())
# print(corrida)

def momento():
    data_e_hora_atuais = datetime.now()
    data_e_hora_em_texto = data_e_hora_atuais.strftime('%H:%M %d/%m/%Y')
    return data_e_hora_em_texto


    
    