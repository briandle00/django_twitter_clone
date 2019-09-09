from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .forms import SignUpForm, LogInForm

# Create your views here.
def home(request):
	signupform = SignUpForm()
	loginform = LogInForm()
	return render(request, '../templates/frontpage.html', {'signupform': signupform, 'loginform': loginform})