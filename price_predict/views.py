from django.shortcuts import render
from .models import Price


# Create your views here.
def landing(request):
    price_info = Price.objects.all()
    return render(
        request,
        'index.html',
        {
            'price_info': price_info,
        }
    )
