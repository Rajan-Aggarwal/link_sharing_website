from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def signup(request):
	if request.method=="POST":
		username = request.POST['username']
		password = request.POST['pass1']
		password_check = request.POST['pass2']
		if password == password_check:
			try:
				user = User.objects.get(username=username)
				return render(request, 'accounts/signup.html', {'msg':'username already exists. try again'})
			except User.DoesNotExist:
				user = User.objects.create_user(username, password=password)
				return render(request, 'accounts/login.html', {'msg':'successfully registered. login here'})
		else:
			return render(request, 'accounts/signup.html', {'msg':'couldn\'t match passwords. try again'})
	else:
		return render(request, 'accounts/signup.html')

def signin(request):
	if request.method=="POST": 
		username = request.POST['username']
		password = request.POST['pass']
		user = authenticate(request, username=username, password=password) #gives a User object
		if user is not None:
			login(request, user)
			if 'next' in request.POST: #if request.POST['next'] exists
				return redirect(request.POST['next']) 
			return redirect('home')
		else:
			return render(request, 'accounts/login.html', {'msg':'invalid username or password'})
	else:
		return render(request, 'accounts/login.html')

def logout_view(request):
	logout(request)
	return redirect('home')
