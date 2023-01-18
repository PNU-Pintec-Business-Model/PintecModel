from django.shortcuts import render
from datetime import datetime
from dateutil.relativedelta import relativedelta
from .models import Price


# Create your views here.
def landing(request):
    # now = datetime.now()
    # week = []
    # for i in range(7):
    #     week.append((now + relativedelta(days=-i).date()))
    # now.date()
    # week_info = Price.objects.filter(datas__in=week)

    price_info = Price.objects.all()
    return render(
        request,
        'index.html',
        {
            'price_info': price_info,
            # 'week_info': week_info,
        }
    )


def kakao(request):
    return render(
        request, 'layout-kakao.html'
    )



