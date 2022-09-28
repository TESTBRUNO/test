from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.db import IntegrityError
from django.contrib import messages



#возвращает страницу успешной регистрации или форму регистрации
def reg_page(request):
	if request.method == 'POST':
		form = request.POST
		name = form['name']


		if not User.objects.filter(username__exact=name).exists():
			user = User.objects.create_user(name, form['email'], form['password'])
			user.save()
			if user is not None:
				return render(request, "successful-reg.html")
		else:
			return render(request, 'idi.html')


		# try:
		# 	user = User.objects.create_user(form['name'], form['email'], form['password'])
		# 	user.save()
		# 	if user is not None:
		# 		return render(request, "successful-reg.html")
		# except IntegrityError:
		# 	return render(request, 'idi.html')

	return render(request, 'registration-form.html')


#возвращает страницу успешной аутентификации
def auth_page(request):
	if request.method == 'POST':
		form = request.POST
		user = authenticate(username=form['name'], password=form['password'])
		if user is not None:
			request.session['for_auth'] = 'h' #создает сессию
			return render(request, "sucess_auth.html" , {'m':request.session['for_auth']})
		if user == None:
			messages.add_message(request, messages.INFO, 'Hello world.')
			return render(request, "auth-form.html" )

		if request.session['for_auth'] == 'h':
			return render(request, "sucess_auth.html")
		else:
			return render(request, 'auth-form.html')

	if request.method == "GET":
		return render(request, 'auth-form.html')

def test_p(request):
	return render(request, 'testsa.html')

# Create your views here.
