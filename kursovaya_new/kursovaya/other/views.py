from django.shortcuts import render


# Create your views here.

# поведение работы сайта при переходе на страницы


def homepage(request):
    return render(request, 'homepage.html')

def contacts(request):
    return render(request, 'contacts.html')

def about_the_company(request):
    return render(request, 'about_the_company.html')