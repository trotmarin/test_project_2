from django.shortcuts import render
from .models import HelloWorld

# Create your views here.

def test_view(request):
    print('서무의 달인')




    return render(request, 'test.html')