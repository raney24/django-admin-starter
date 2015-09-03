from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.template import RequestContext
from starter.forms import LoginForm 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/accounts/register/complete')

	else:
		form = UserCreationForm()
	token = {}
	token.update(csrf(request))
	token['form'] = form

	return render_to_response('registration/registration_form.html', token)

def home(request):
	return render_to_response('index.html', 
							{'username': request.user.username})
    
def about(request):
	return render_to_response('about.html',
						{'username': request.user.username})

def login(request):
    message = None
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return HttpResponseRedirect('/accounts/loggedin')
            else:
                message = "Invalid username and/or password, please reenter"
    else:
        form = LoginForm()
    return render_to_response('registration/login.html', {'message': message, 'form': form},
                            context_instance=RequestContext(request))

def process_login(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)

	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/accounts/loggedin')
	else:
		return HttpResponseRedirect('/accounts/login_error')

def login_error(request):
	return render_to_response('registration/login_error.html')

def loggedin(request):
	return render_to_response('registration/loggedin.html',
								{'username': request.user.username})

def logout(request):
	auth.logout(request)
	return render_to_response('registration/logged_out.html')

@login_required
def restricted(request):
	return render_to_response('restricted.html',)






