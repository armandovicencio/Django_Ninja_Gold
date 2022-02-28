from django.shortcuts import render, redirect, reverse


def bienvenido(request):
    if request.method == "GET":
        return render(request, 'Inicio/index.html')

    if request.method == "POST":
        # hacer una validacion
        if (request.POST['oro'] != '') and (request.POST['movimientos'] != ''):
            print(request.POST['oro'])
            request.session['oro'] = request.POST.get('oro', 150)
            request.session['movimientos'] = request.POST.get('movimientos', 5)
            request.session['goldstatus'] = 0
            request.session['contador'] = 0
            request.session['estado'] = False
            request.session['activities'] = []
            request.session['winlost'] = ''
            return redirect(reverse('juego:money'))
        else:
            red = 'red'
            color = f'style = "color:{red} "'
            request.session['mensaje'] = f'<h3 {color} >Please select your gold and moves! :)</h3>'
            context = {
                'mensaje': request.session['mensaje']
            }
            return render(request, 'Inicio/index.html', context)