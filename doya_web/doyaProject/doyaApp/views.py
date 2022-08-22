from django.shortcuts import render, redirect

from .models import Profile
from django.contrib.auth.models import User
from django.contrib import auth


import os
import pandas as pd
import numpy as np
import glob
import random
import sklearn


# Create your views here.

def home(request):

    context = {
            'random_news_data_num1' : None,
            'random_news_data_lst' : None,
            'recent_news_data_num1': None,
            'recent_news_data_lst': None
        } 



    user_major = None
    

    data_path = r'C:\Users\KOH_AI\Documents\git_Dasktop\2020_News_Bigdata_HACKATHON\doya_web\doyaProject\doyaApp\data'
    major_fold = os.listdir(data_path)                    

    # data_path = r'C:\Users\MyLaptop\Desktop\개발\2020_News_Bigdata_HACKATHON\doya_web\doyaProject\doyaApp\data'
    # major_fold = os.listdir(data_path)                    

    # print(major_fold)

    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)  
        profile = Profile.objects.filter(user=user).get() 
        # print(user, profile.user_major)
    #--------------------------------------------------------------------------------------------#
        # for major in major_fold:
        #     if profile.user_major == major:
        #         user_major = major
        #         break

        # news_dir = os.path.join(data_path, user_major)
        # news_fold = os.listdir(news_dir)

        # os.chdir(news_dir)
        # print(news_fold)
        # recently_news_file = glob.glob('2020_*.csv')
        # print(recently_news_file)

        # news_data = pd.read_csv(recently_news_file[0], error_bad_lines=False, engine="python", encoding='utf-8')
        # print(news_data.columns)

        # recently_news_lst_num1 = news_data.iloc[0]
        # recently_news_lst = news_data.iloc[1:5]

        # print(recently_news_lst_num1)
        # print(recently_news_lst)

        # df_shuffled=sklearn.utils.shuffle(news_data)
        # df_shuffled=sklearn.utils.shuffle(df_shuffled)
        # random_news_lst_num1 = df_shuffled.iloc[0]
        # random_news_lst = df_shuffled.iloc[1:5]
        
        # print(random_news_lst_num1)
        # print(random_news_lst)

# ------------------------------------------------------------------------------------------------

        random_news_data = pd.read_csv(r'C:\Users\KOH_AI\Documents\git_Dasktop\2020_News_Bigdata_HACKATHON\doya_web\doyaProject\doyaApp\data\전산학&컴퓨터\2020_news_part_data.csv', encoding='utf-8')
        recent_news_data = pd.read_csv(r'C:\Users\KOH_AI\Documents\git_Dasktop\2020_News_Bigdata_HACKATHON\doya_web\doyaProject\doyaApp\data\전산학&컴퓨터\2020_news_data.csv', encoding='utf-8')
        
        random_news_data_num1 = random_news_data.iloc[0]
        random_news_data_lst = random_news_data.iloc[1:5]

        recent_news_data_num1 = recent_news_data.iloc[0]
        recent_news_data_lst = recent_news_data.iloc[1:5]


        context['random_news_data_num1'] = random_news_data_num1
        context['random_news_data_lst'] = random_news_data_lst
        context['recent_news_data_num1'] = recent_news_data_num1
        context['recent_news_data_lst'] = recent_news_data_lst


    return render(request, 'home.html', context)



def news_list(request):
    
    random_news_data = pd.read_csv(r'C:\Users\MyLaptop\Desktop\개발\2020_News_Bigdata_HACKATHON\doya_web\doyaProject\doyaApp\data\전산학&컴퓨터\2020_news_part_data.csv', encoding='utf-8')
    recent_news_data = pd.read_csv(r'C:\Users\MyLaptop\Desktop\개발\2020_News_Bigdata_HACKATHON\doya_web\doyaProject\doyaApp\data\전산학&컴퓨터\2020_news_data.csv', encoding='utf-8')
    
    random_news_data_lst = random_news_data.iloc[:10]
    print('--------------------------@@@@@@@@@@@@@@@@@@@@@@')
    print(random_news_data_lst)


    recent_news_data_lst = recent_news_data.iloc[:10]

    context = {
            'random_news_data_lst' : random_news_data_lst,
            'recent_news_data_lst': recent_news_data_lst
        } 

    return render(request, 'news_list.html', context)

def news_list2(request):
    return render(request, 'news_list2.html')

def login(request):
    
    if request.method == 'POST':
        user_id = request.POST['user_id']
        user_pw = request.POST['user_pw']
        user = auth.authenticate(request, username=user_id, password=user_pw)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error' : 'username or password is incorrect'})

    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('home')

major_lst = ['간호', '건축', '경영', '공예', '관광', '광고', '교육', '교통&운송', '기계&금속',
    '농림&수산', '도시&토목', '디자인', '미술', '법', '뷰티아트', '사진&만화', '사회과학',
    '산업공학', '생명과학', '서비스', '소재&재료', '수의학', '식품', '약학', '언론', '언어&문학', '에너지', '연극&영화',
    '영상&예술', '유아교육', '음악', '응용소프트웨어', '의류', '인문과학', '자연과학', '전기&전자',
    '전산학&컴퓨터', '정보&통신', '조선', '체육', '초등교육', '치료&보건', '특수교육', '화공']

def signup(request):
    if request.method == 'POST':
        if request.POST['user_pw'] == request.POST['user_pw_check']:
            user = User.objects.create_user(
                username=request.POST['user_id'],
                password=request.POST['user_pw'],
                email=request.POST['user_email']
            )
            user_name = request.POST['user_name']
            user_phone_num = request.POST['user_phone_num']
            user_major = request.POST['major_lst']

            profile = Profile(user=user,
                            user_name=user_name,
                            user_phone_num=user_phone_num,
                            user_major=user_major)
            profile.save()
            auth.login(request, user)
            return redirect('login')
        return render(request, 'signup.html')

    context = {
        'major_lst' : major_lst
    }
    return render(request, 'signup.html', context)



def news_list(request):

    
    return render(request, 'news_list.html')


def mypage(request):
    return render(request, 'mypage.html')

def list(request):
    return render(request, 'news_list.html')

def scrapbook(request):
    return render(request, 'scrapbook.html')

def scrapB1(request):
    return render(request, 'scrapB1.html')

def mypaga(request):
    return render(request, 'mypaga.html')
