from pickle import NONE
from django.shortcuts import render, HttpResponse, redirect, reverse
import datetime
import random


def index(request):
    return redirect(reverse('Inicio:index'))


def procesar(request, valor=''):
    print(f"desde procesar:{request.get_full_path()}")
    building = valor
    # AL ENVIAR POR FORMULARIO, NO EXISTE "VALOR" QUE VENDRIA DE BOTON DE ENLACE, POR LO QUE LLEGA VACIO POR DEFECTO
    # EN ESE CASO VALOR BUILDING TOMA EL VALUE DEL FORMULARIO
    if valor == '':
        building = request.POST['building']

    # se declaran los colores utilizados en los mensajes
    green = 'green'
    red = 'red'

    # se guarda en una variable el metodo para trabajar con fecha y horas
    date = datetime.datetime.now()

    # se obtiene el formato requerido para la hora y fecha
    datemoment = f'{date.strftime("%Y")}/{date.strftime("%m")}/{date.strftime("%d")} {date.strftime("%I")}:{date.strftime("%M")} {date.strftime("%p")}'

    # una lista de diccionarios con los VALUE esperadas desde el html y los parametros de valores maximos y minimos que se UTILIZARAN como parametros en el metodo RANDOM
    # para obtener numero aleatorios
    diccionario = [{'name': 'farm', 'min': 10, 'max': 20}, {'name': 'cave', 'min': 5, 'max': 10}, {
        'name': 'house', 'min': 2, 'max': 5}, {'name': 'casino', 'min': -50, 'max': 50}]

    # se recorre la lista de diccionarios y se realiza la logica
    for i in range(4):
        numero = 0
        if diccionario[i]["name"] == building:
            numero = int(
                round(random.random()*(((diccionario[i]["max"])-(diccionario[i]["min"])))+(diccionario[i]["min"])))
            print(
                f" soy el nuemro random {numero} desde {building}")
            request.session['goldstatus'] += numero
            request.session['contador'] += 1

            if (building == 'farm') or (building == 'cave') or (building == 'house'):
                form = building
                color = f'style = "color:{green} "'
                mensaje = f'<h5 {color}>Earned {numero} golds from the {form}! {datemoment}</h5>'
                request.session['activities'].append(mensaje)
            else:
                if((building == 'casino') and numero >= 0):
                    form = building
                    color = f'style = "color:{green} "'
                    mensaje = f'<h5 {color}>Entered a {form} and win {numero} golds...you are lucky! {datemoment}</h5>'
                    request.session['activities'].append(mensaje)
                else:
                    form = building
                    color = f'style = "color:{red} "'
                    mensaje = f'<h5 {color}>Entered a {form} and lost {numero} golds... Ouch... {datemoment}</h5>'
                    request.session['activities'].append(mensaje)

            if (request.session['goldstatus'] < int(request.session['oro'])):
                if((int(request.session['movimientos'])-request.session['contador']) <= 0):
                    request.session['estado'] = True
                    color = f'style = "color:{red} "'
                    request.session['winlost'] = f'<h1 {color} >YOU LOST :(</h1>'

            if (request.session['goldstatus'] >= int(request.session['oro'])):
                if((int(request.session['movimientos'])-request.session['contador']) >= 0):
                    request.session['estado'] = True
                    movimientostotales = request.session['contador']
                    color = f'style = "color:{green} "'
                    request.session['winlost'] = f'<h1 {color} >YOU WIN WITH {movimientostotales} MOVES :)</h1>'
    # los valores obtenido se guardan en session para ser mostrados con el metodo process_money
    return redirect('/process_money')


def process_money(request):
    # Todo las variables de session estan guardadas en el siguiente contexto
    context = {
        'goldstatus': request.session['goldstatus'],
        'estado': request.session['estado'],
        'contador': request.session['contador'],
        'actividad': request.session['activities'],
        'metaoro': request.session['oro'],
        'metamovimientos': request.session['movimientos'],
        'movimientostotal': int(request.session['movimientos']) - request.session['contador'],
        'winlost': request.session['winlost']
    }
    return render(request, 'app/index.html', context)

