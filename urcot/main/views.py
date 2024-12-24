from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	# data = {
	# 	'title':'Главная страница',
	# 	'values': ['Some', 'Hello', '123']
	# }
	return render(request, 'main/index.html')

def about_us(request):
	return render(request, 'main/about_us.html')

# def efls(request):
# 	return HttpResponse("<h4>EVERYTHING FOR LABOR SAFETY or ВCЁ ДЛЯ ОХРАНЫ ТРУДА</h4>")

# def about_organization(request):
# 	return HttpResponse("<h4>Об организации</h4>")

def manager(request):
	return render(request, 'main/manager.html')


def literature(request):
	return render(request, 'main/literature.html')

def services(request):
	return render(request, 'main/services.html')

def personal_account(request):
	return render(request, 'main/personal_account.html')

