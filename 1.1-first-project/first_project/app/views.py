from django.http import HttpResponse
from django.shortcuts import render, reverse
from os import listdir
from os.path import isfile, join
import datetime


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    date = datetime.datetime.today()
    current_time = date.strftime('%H:%M')
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей 
    # директории
    files = [f for f in listdir(r'C:\Users\Olesya.Dzhafarova\dj-homeworks') if isfile(join(r'C:\Users\Olesya.Dzhafarova\dj-homeworks', f))]
    msg = f'Файлы рабочей директории: {files}'
    return HttpResponse(msg)
    # raise NotImplemented
