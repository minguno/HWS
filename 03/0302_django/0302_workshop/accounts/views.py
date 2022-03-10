from django.shortcuts import render

# Create your views here.
def index(request):
    # accounts 폴더 안에 이중으로 넣었기 때문에 경로를 붙여줘야 한다
    return render(request, 'accounts/index.html')