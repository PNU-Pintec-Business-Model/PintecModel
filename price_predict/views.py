from django.shortcuts import render
from datetime import datetime
from dateutil.relativedelta import relativedelta
from .models import Price
import csv
import pandas as pd

price_info = Price.objects.all()


# Create your views here.
def landing(request):
    # now = datetime.now()
    # week = []
    # for i in range(7):
    #     week.append((now + relativedelta(days=-i).date()))
    # now.date()
    # week_info = Price.objects.filter(datas__in=week)

    return render(
        request,
        'index.html',
        {
            'price_info': price_info,
        }
    )


def kakao(request):
    return render(
        request, 'layout-kakao.html'
    )


def dbrequest(request):
    with open("D:/csvdata/update_data0.csv", 'r', encoding="UTF-8") as f:
        dr = csv.DictReader(f)
        s = pd.DataFrame(dr)
    ss = []
    for i in range(len(s)):
        st = (s["DELNG_DE"][i], s["MRKT_NM"][i], s["CPR_NM"][i], s["PRDLST_NM"][i],s["SPCIES_NM"][i],
              s["GRAD"][i], s["weight"][i], s["PRI_MAX"][i], s["PRI_MIN"][i], s["PRI_AVE"][i], s["PRI_PRED"][i])
        ss.append(st)
    for i in range(len(s)):
        Price.objects.create(DELNG_DE=ss[i][0], MRKT_NM=ss[i][1], CPR_NM=ss[i][2], PRDLST_NM=ss[i][3], SPCIES_NM=ss[i][4]
                                , GRAD=ss[i][5], weight=ss[i][6], PRI_MAX=ss[i][7], PRI_MIN=ss[i][8], PRI_AVE=ss[i][9], PRI_PRED=ss[i][10])

    return render(
        request,
        'index.html',
        {
            'price_info': price_info,
        }
    )

def aipred(request):
