from django.shortcuts import render
from .models import Price
import csv
import tensorflow as tf
import pandas as pd
import numpy as np
from pickle import load

price_info = Price.objects.all()
datasize = 2  # 풋고추0, 새송이1
predict_result = []  # 풋고추, 새송이
good_list = []
company_list = []
ori_data = []


def setting_data(request):
    data = []
    x_shift_data = []  # 평균가가 shift된 입력 데이터 (input)
    x_input_data = []
    model = []
    x_sc = []
    y_sc = []
    good = []
    company = []

    for i in range(datasize):
        ori_data.append(pd.read_csv('./price_predict/csvdata/update_data{}.csv'.format(i)))
        model.append(tf.keras.models.load_model('./price_predict/ai_model/LSTM-model{}_adam.h5'.format(i)))
        x_sc.append(load(open('./price_predict/ai_model/x_sc{}.pkl'.format(i), 'rb')))
        y_sc.append(load(open('./price_predict/ai_model/y_sc{}.pkl'.format(i), 'rb')))
        data.append(ori_data[i].sort_values(by=['DELNG_DE'])[['DELNG_DE', 'PRI_AVE']])

    for i in range(datasize):
        for j in range(len(ori_data[i])):
            good.append(ori_data[i]["PRDLST_NM"][j])
            company.append(ori_data[i]["CPR_NM"][j])

    good = list(set(good))
    company = list(set(company))

    for i in range(len(good)):
        good_list.append(good[i])

    for i in range(len(company)):
        company_list.append(company[i])

    for i in range(datasize):
        x_shift_data.append(ori_data[i].groupby('DELNG_DE', as_index=False)['PRI_AVE'].mean())  # 날짜별 평균값 리스트
        x_shift_data[i]['PRI_AVE'] = round(x_shift_data[i]['PRI_AVE'], 2)

    for i in range(datasize):
        temp = x_shift_data[i][-10:]['PRI_AVE'].tolist()
        temp.reverse()
        x_input_data.append(np.array(temp).reshape(1, -1))

    for i in range(datasize):
        x_data_sc = x_sc[i].transform(x_input_data[i])
        predict_result.append(y_sc[i].inverse_transform(model[i].predict(x_data_sc))[0][0])

    return render(
        request,
        'index.html',
        {
            'price_info': price_info,
            'predict_result': predict_result,
            'good_list': good_list,
            'company_list': company_list,
        }
    )


# Create your views here.
def landing(request):

    return render(
        request,
        'index.html',
        {
            'price_info': price_info,
            'predict_result': predict_result,
            'good_list': good_list,
            'company_list': company_list,
        }
    )


def kakao(request):
    return render(
        request, 'layout-kakao.html'
    )


def dbrequest(request):
    Price.objects.all().delete()
    for i in range(datasize):
        with open("./price_predict/csvdata/update_data{}.csv".format(i), 'r', encoding="UTF-8") as f:
            dr = csv.DictReader(f)
            s = pd.DataFrame(dr)
        ss = []
        for j in range(len(s)):
            st = (s["DELNG_DE"][j], s["MRKT_NM"][j], s["CPR_NM"][j], s["PRDLST_NM"][j],s["SPCIES_NM"][j],
                  s["GRAD"][j], s["weight"][j], s["PRI_MAX"][j], s["PRI_MIN"][j], s["PRI_AVE"][j], s["PRI_PRED"][j])
            ss.append(st)
        for j in range(len(s)):
            Price.objects.create(DELNG_DE=ss[j][0], MRKT_NM=ss[j][1], CPR_NM=ss[j][2], PRDLST_NM=ss[j][3],
                                 SPCIES_NM=ss[j][4], GRAD=ss[j][5], weight=ss[j][6], PRI_MAX=ss[j][7], PRI_MIN=ss[j][8],
                                 PRI_AVE=ss[j][9], PRI_PRED=ss[j][10])

    return render(
        request,
        'index.html',
        {
            'price_info': price_info,
            'predict_result': predict_result,
            'good_list': good_list,
            'company_list': company_list,
        }
    )

def predict0(request, company) :
    
    companylist=['중앙청과', '서울청과', '동화청과', '농협가락(공)', '한국청과']
    """
    f = open("./price_predict/csvdata/update_data0.csv", 'r', encoding="UTF-8")
    dr = csv.DictReader(f)
    s = pd.DataFrame(dr)
    ss=[]
    for j in range(len(s)) :
        if s["CPR_NM"][j]==companylist[int(company)] :
            st = (s["DELNG_DE"][j], s["MRKT_NM"][j], s["CPR_NM"][j], s["PRDLST_NM"][j],s["SPCIES_NM"][j],
                  s["GRAD"][j], s["weight"][j], s["PRI_MAX"][j], s["PRI_MIN"][j], s["PRI_AVE"][j], s["PRI_PRED"][j])
            ss.append(st)
    """
    price_info0 = Price.objects.filter(CPR_NM=companylist[int(company)], PRDLST_NM='풋고추')
            
    return render(
        request,
        'index.html',
        {
            'price_info': price_info0,
            'predict_result': predict_result,
            'good_list': good_list,
            'company_list': company_list,
        }
    )
    
def predict1(request, company) :
    companylist=['중앙청과', '서울청과', '동화청과', '농협가락(공)', '한국청과']

    price_info1 = Price.objects.filter(CPR_NM=companylist[int(company)], PRDLST_NM='새송이')
    
    return render(
        request,
        'index.html',
        {
            'price_info': price_info1,
            'predict_result': predict_result,
            'good_list': good_list,
            'company_list': company_list,
        }
    )