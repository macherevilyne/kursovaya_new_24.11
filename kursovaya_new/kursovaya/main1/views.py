from django.shortcuts import render
from .models import Actual  #
from django.core.paginator import Paginator


def actual(request):  # функция запроса
    cargo = Actual.objects.get_queryset().order_by('id')  # получение кверисет всех обьектов, полей из созданных записей
    paginator = Paginator(cargo, 6)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()
    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''
    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {
        "cargo": page, # запись их в контексный словарь
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url
    }

    return render(request, 'actual.html', context)  # возвращение слова и вывод в шаблон


def carrier(request):
    return render(request, 'carrier.html')
