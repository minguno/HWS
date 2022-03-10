from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')


def dinner(request, menu, number):
    context = {
        'menu': menu,
        'number': number,
    }
    return render(request, 'pages/dinner.html', context)