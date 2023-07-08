from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'main/index.html')

def board(request):
    return render(request, 'main/board.html')